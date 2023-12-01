from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class Question(BaseModel):
    id: Optional[int] = None

class ReadQuestion(Question):
    text_id: int
    question: str

class ReadQuestionForText(Question):
    question: str

class CreateUpdateQuestion(Question):
    text_id: int
    question: str

