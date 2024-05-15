
from pydantic import BaseModel,Field

class Item(BaseModel):
    subject: str=Field(None,examples=["Math"])
    topic: str=Field(None,examples=['Algebra'])
    lesson_title: str=Field(None,examples=['Algebra'])
    summary: str=Field(None,examples=['Algebra'])
    context: str=Field(None,examples=['Algebra'])
    subtopic: str=Field(None, examples=['Linear Equation'])

class CurrentModel(BaseModel):
    gpt_model_name: str = Field(None, examples=[
        "gpt-4-0613",
        "gpt-4",
        "gpt-3.5-turbo-0613",
        "gpt-4-1106-preview",
        "gpt-3.5-turbo-1106",
        "gpt-4o" 
    ])
