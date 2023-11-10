
from pydantic import BaseModel,Field

class Item(BaseModel):
    subject: str=Field(None,examples=["Math"])
    topic: str=Field(None,examples=['Algebra'])
    lesson_title: str=Field(None,examples=['Algebra'])
    summary: str=Field(None,examples=['Algebra'])
    context: str=Field(None,examples=['Algebra'])
    subtopic: str=Field(None, examples=['Linear Equation'])

    