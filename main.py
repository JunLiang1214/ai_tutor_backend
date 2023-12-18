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
    print('--------------------------------------');
    print('hellloo begin_chat', item)
    print('--------------------------------------');
    agent_system_message = getSystemPrompt(item)
    conversation.add_message("system",agent_system_message)
    response = conversation.chat_completion_request(messages=conversation.conversation_history)
#     response= {'role': 'assistant', 'content': """# Lesson Brief
# 
# Welcome to our lesson on the Four Basic Operations of Maths! Today, we will explore the foundational operations that are crucial for understanding and working with numbers: addition, subtraction, multiplication, and division. This fundamental knowledge is essential for everyday calculations as well as for pursuing more advanced topics in mathematics.
# 
# # Introduction to the Topic
# 
# In mathematics, the four basic operations are the building blocks that allow us to perform calculations with numbers. They are:
# 
# - **Addition (+)**: Combining two or more numbers to get a larger number (total or sum).
# - **Subtraction (-)**: Taking one number away from another to find the difference.
# - **Multiplication (×)**: Adding a number to itself a certain number of times, which gives the product.
# - **Division (÷)**: Splitting a number into equal parts or groups, resulting in the quotient.
# 
# These operations are performed on numbers known as "operands". In the expression `5 + 3`, the numbers 5 and 3 are operands, and the `+` symbol represents the operation (addition in this case).
# 
# ## Importance
# 
# Understanding these operations is key to solving basic arithmetic problems, which you'll encounter not only in school but in many real-life situations such as shopping, cooking, and budgeting. They are also the foundation for more complicated math concepts like algebra, calculus, and beyond.
# 
# ## Symbols and Terms
# 
# | Operation     | Symbol | Example | Term           |
# |---------------|:------:|:-------:|----------------|
# | Addition      |   +    | 7 + 3   | Sum or Total   |
# | Subtraction   |   -    | 7 - 3   | Difference     |
# | Multiplication|   ×    | 7 × 3   | Product        |
# | Division      |   ÷    | 7 ÷ 3   | Quotient       |
# 
# Each operation also has a reverse operation:
# 
# - Addition's reverse operation is **Subtraction**.
# - Multiplication's reverse operation is **Division**.
# 
# Understanding how these operations relate to each other allows us to solve for unknown numbers, rearrange equations, and more.
# 
# ---
# 
# Do you understand the introduction to the four basic operations of mathematics?"""}
#     response= {'role': 'assistant', 'content': """# Lesson Brief
# 
# Welcome to our lesson on the Four Basic Operations of Maths! Today, we will 
# Today we will be learning about the four basic operations in mathematics. These operations include addition, subtraction, multiplication, and division. We will discuss what each operation means and how to perform calculations using these operations.\n\n ## Introduction to the Topic\n The four basic operations in mathematics are essential for performing calculations. They are used in various mathematical problems, including arithmetic, algebra, and more advanced mathematical concepts. Understanding these operations is crucial for building a strong foundation in mathematics.\n\nDo you understand the importance of the four basic operations in mathematics?'"""}

    # print('--------------------------------------');
    # print('response=',response);
    # print('--------------------------------------');
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