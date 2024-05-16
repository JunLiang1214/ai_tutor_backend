import json
from Tools.gpt_model_config import ModelConfigKeysEnum, get_model_config
from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import FastAPI,HTTPException, Request,UploadFile,File,Form
from models.models import Item, CurrentModel
from GptLLM.gpt import GPTLLm
from Tools.prompts import  getSystemPrompt
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse,JSONResponse
from openai import OpenAI
from pathlib import Path
import aiofiles
import logging
from io import BytesIO
from typing import List
import json
import pytesseract
from PIL import Image

conversation = GPTLLm()
client = OpenAI()

app = FastAPI()
UPLOAD_FOLDER = "uploads"

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
class TextToSpeechRequest(BaseModel):
    text: str
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Ensure the uploads folder exists
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        
        # Read the file content
        contents = await file.read()
        
        # Save the file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(contents)
        
        return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)
    
class ConversationHistory(BaseModel):
    messages: List[dict]
@app.post("/sendImage")
async def send_image(image: str = File(...), conversation_history: str = Form(...)):
    print(image)

    # Ensure the uploads folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            
    # Save the file locally
    image_path = os.path.join(UPLOAD_FOLDER, image)
    print(image_path)
    # Perform OCR on the image
    ocr_text = pytesseract.image_to_string(Image.open(image_path))
    print(ocr_text)
    conversation.add_message("user",ocr_text)
    response = conversation.chat_completion_request(messages=conversation.conversation_history)    
    conversation.add_message(response['role'],response['content'])
    # conversation.display_conversation()
    return {"message":response['content']}

@app.post("/audio")
async def generate_audio(request: TextToSpeechRequest):
    text = request.text
    logging.info(f"Received text: {text}")
    speech_file_path = Path("speech.mp3")  # Use Path from pathlib

    try:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="alloy",
            input=text
        )
        logging.info("Speech generation response received.")

        # Use stream_to_file method to save the file
        response.stream_to_file(speech_file_path)

        if not speech_file_path.exists():
            raise HTTPException(status_code=500, detail="Error generating speech file")

        logging.info("Returning audio file response.")
        return FileResponse(speech_file_path, media_type="audio/mpeg", filename="speech.mp3")
    except Exception as e:
        logging.error(f"Error generating speech: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating speech: {str(e)}")

@app.post('/begin_chat')
async def begin_chat(item:Item):  
    print('--------------------------------------');
    print('hellloo begin_chat', item)
    print('--------------------------------------');
    agent_system_message = getSystemPrompt(item)
    print('agent_system_message=',agent_system_message);
    conversation.add_message("system",agent_system_message)
    response = conversation.chat_completion_request(messages=conversation.conversation_history)
    print('--------------------------------------');
    print('RESPONSE["role"]=',response["role"]);
    print('--------------------------------------');
    if response:
        conversation.add_message(response['role'],response['content'])
        return {"message":response['content']}
    return {"message":"there was an error"}

@app.post('/chat')
async def chat(message:str):  
    conversation.add_message("user",message)
    response = conversation.chat_completion_request(messages=conversation.conversation_history)    
    conversation.add_message(response['role'],response['content'])
    # conversation.display_conversation()
    return {"message":response['content']}

@app.get('/')
async def check():
    return "hello world"
@app.get('/change_model/{gpt_model_name}', 
         summary="Change the model",
         description='Change the current AI model to one of the available models: "gpt-4-0613", "gpt-4-0125-preview", "gpt-4", "gpt-3.5-turbo", "gpt-4-1106-preview", "gpt-3.5-turbo-1106"',
         response_description="The result of the model change operation")
async def change_model_route(gpt_model_name: str):
    
    # Read the current configuration from the JSON file
    with open('Tools/model_config.json', 'r') as file:
        config = json.load(file)

    # Check if the gpt_model_name is in the available_models list
    if gpt_model_name in config[ModelConfigKeysEnum.AVAILABLE_MODELS.value]:
        # Update the current_model in the config
        config[ModelConfigKeysEnum.CURRENT_MODEL.value] = gpt_model_name

        # Write the updated configuration back to the JSON file
        with open('Tools/model_config.json', 'w') as file:
            json.dump(config, file, indent=4)

        return {"message": f"Model changed to {gpt_model_name}"}
    else:
        return {"error": f"Model {gpt_model_name} not found"}

# todo
## add models
## get models list