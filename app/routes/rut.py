from typing import Any, Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.text import TextForQuestion
from ml.model import generate
from dependencies import get_db
from crud.question import question_crud
from schemas.text import ReadText

router = APIRouter(prefix="/rut", tags=["rut"])

@router.post("/generate")
def generate_questions(item: TextForQuestion) -> list[str]:
    """
    Генерация вопросов по контексту.
    """
    question = generate(item.text, item.quantity)
    return question

@router.post("/generate_save", response_model=ReadText)
def generate_questions_save(item: TextForQuestion, db: Session = Depends(get_db)):
    """
    Генерация вопросов по контексту с их сохранением.
    """
    questions = generate(item.text, item.quantity)
    text = question_crud.create_with_text(db, text=item.text, questions=questions)
    return text