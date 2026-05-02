"""
API Model to read input from user
"""

import uuid
from pydantic import BaseModel

class SessionState(BaseModel):
    """
    Information that persist throughout the session or until event-based or time-based changes happen.
    """
    session_id: uuid.UUID
    user_id: str
    create_at: str
    last_active: str
    topic: str
    game_level: int | None = None
    history: str
    summary: str
