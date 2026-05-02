"""
API Model to read input from user
"""

from pydantic import BaseModel

class RequestSubmission(BaseModel):
    """
    Code
    """
    session_id: int | None = None
    body: str
