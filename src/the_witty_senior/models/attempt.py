"""
API Model to read input from user
"""

from pydantic import BaseModel

class CodeSubmission(BaseModel):
    """
    Code
    """
    task_id: int
    code: str
