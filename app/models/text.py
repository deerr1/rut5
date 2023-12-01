from sqlalchemy import Column, Integer, ForeignKey, String, Text, Numeric, Date, Time, Boolean
from sqlalchemy.orm import relationship

from db.database import Base


class Text(Base):
    __tablename__ = "text"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

    question = relationship("Question", back_populates="text", cascade="all, delete")