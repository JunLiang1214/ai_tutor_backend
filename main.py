import json
from Tools.gpt_model_config import ModelConfigKeysEnum, get_model_config
from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import FastAPI, Path
from models.models import Item, CurrentModel
from GptLLM.gpt import GPTLLm
from Tools.prompts import  getSystemPrompt
from fastapi.middleware.cors import CORSMiddleware

conversation = GPTLLm()

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

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