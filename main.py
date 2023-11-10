from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import FastAPI 
from models.models import Item
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
    print('hellloo begin_chat', item)
    agent_system_message = getSystemPrompt(item)
    conversation.add_message("system",agent_system_message)
    response = conversation.chat_completion_request(messages=conversation.conversation_history)
    print('--------------------------------------');
    print('response=',response);
    print('--------------------------------------');
    
    conversation.add_message(response['role'],response['content'])
    return {"message":response['content']}

@app.post('/chat')
async def chat(message:str):  
    conversation.add_message("user",message)
    response = conversation.chat_completion_request(messages=conversation.conversation_history)    
    conversation.add_message(response['role'],response['content'])
    # conversation.display_conversation()
    return {"message":response['content']}
