from sqlalchemy.orm import Session
from datetime import datetime, timezone
from typing import List

from crud.base import CRUDBase
from models.question import Question
from models.text import Text
from schemas.question import ReadQuestion, CreateUpdateQuestion
from schemas.text import ReadText


class CRUDQuestion(CRUDBase[Question, ReadQuestion, CreateUpdateQuestion]):
    def create_with_text(self, db: Session, *, text: str, questions: list[str]) :
        text = Text(text=text)
        db.add(text)
        db.flush()
        question_model_list = []
        for q in questions:
            question = Question(text_id=text.id, question=q)
            question_model_list.append(question)

        db.add_all(question_model_list)
        db.commit()
        db.refresh(text)

        return text

question_crud = CRUDQuestion(Question)



