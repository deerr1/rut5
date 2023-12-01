from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from schemas.question import ReadQuestionForText


class Text(BaseModel):
    id: Optional[int] = None

class ReadText(Text):
    text: str
    question: list[ReadQuestionForText]

    class Config:
        from_attributes=True

class CreateUpdateText(Text):
    text: str

class TextForQuestion(BaseModel):
    text: str
    quantity: Optional[int] = 1
