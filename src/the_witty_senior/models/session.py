"""
API Model to read input from user
"""

from pydantic import BaseModel

class SessionState(BaseModel):
    """
    Information that persist throughout the session or until event-based or time-based changes happen.
    """
    session_id: int
    user_id: str
    topic: str
    game_level: int | None = None
    history: str
    summary: str
