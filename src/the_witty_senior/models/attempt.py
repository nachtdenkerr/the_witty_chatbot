"""
API Model to read input from user
"""

from pydantic import BaseModel

class RequestSubmission(BaseModel):
    """
    Code
    """
    task_id: int
    body: str
