"""
API Model to read input from user
"""

from pydantic import BaseModel

class SessionState(BaseModel):
    """
    Information that persist throughout the session or until event-based or time-based changes happen.
    """
    topic: str
    current_task_progression: float
    game_level: int
    user_preference: str
