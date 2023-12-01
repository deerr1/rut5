from sqlalchemy import Column, Integer, ForeignKey, String, Text, Numeric, Date, Time, Boolean
from sqlalchemy.orm import relationship

from db.database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    text_id = Column(Integer, ForeignKey("text.id"))
    question = Column(String, nullable=False)

    text = relationship("Text", back_populates="question", cascade="all, delete")