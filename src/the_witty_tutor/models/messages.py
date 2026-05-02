"""
API Model to read input from user
"""
import uuid
from pydantic import BaseModel

class RequestSubmission(BaseModel):
    """
    Code
    """
    id: uuid.UUID | None = None
    session_id: uuid.UUID | None = None
    timestamp: str
    role: str
    body: str
