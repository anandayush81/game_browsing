from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from .base import Base

class Games(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    plateform = Column(String)
    score = Column(Float)
    genre = Column(String)
    editor_choice = Column(Boolean)

    def __init__(self, title, plat, scr, genre, editor_choice):
        self.title = title
        self.plateform = plat
        self.score = scr
        self.genre = genre
        self.editor_choice = editor_choice
