"""
API Model to read input from user
"""
import uuid
from pydantic import BaseModel

class RequestSubmission(BaseModel):
    """
    Code
    """
    session_id: uuid.UUID | None = None
    body: str
