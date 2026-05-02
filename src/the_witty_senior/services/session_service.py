from the_witty_senior.models.session import SessionState

session_dict = {}

def create_session() -> SessionState:
    """
    Create new session with no history
    """
    new_session = SessionState(session_id=0,
                               user_id="temp_usr",
                               topic="",
                               game_level=0,
                               history="",
                               summary="")
    return new_session

def get_session(session_id: int) -> SessionState:
    """
    Retrieve exsiting session based on ID
    """
    if session_id in session_dict.keys():
        return session_dict[session_id]
    else:
        raise NameError

def update_session(session, user_prompt, llm_response):
    """
    Retain history to improve model response
    """
    session.history.append("User prompt: " + user_prompt + "\n")
    session.history.append("LLM response: " + llm_response + "\n")
