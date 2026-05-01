"""
API Model to read input from user
"""

from pydantic import BaseModel

class User(BaseModel):
    """
    User information
    """
    username: str
    nickname: str
    password: str

