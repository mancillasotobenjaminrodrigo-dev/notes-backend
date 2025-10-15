from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Note(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

class CreatedNote(BaseModel):
    title: str
    content: str