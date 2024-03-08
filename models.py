from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Define your models here


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullalble=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))

    question = relationship("Question", back_populates="answers")

class 
