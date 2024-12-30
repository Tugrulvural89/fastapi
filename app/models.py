from sqlalchemy import Column, Integer, String, Text 
from .database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)

    def __repr__(self):
        return f"Blog(id={self.id}, title={self.title}, content={self.content})"
    