"""
Module docstring
"""

from fastapi import APIRouter
from the_witty_senior.services import session_service, tutor_service
from the_witty_senior.models.attempt import RequestSubmission

router = APIRouter()

@router.post("/tutor")
def tutoring(request: RequestSubmission):
    """
    Submit endpoint that will run and evaluate the code submission from user
    """
    print(request)
    if request.session_id is None:
        session = session_service.create_session()
        session_service.session_dict[session.session_id] = session
    else:
        try:
            session = session_service.get_session(request.session_id)
        except NameError:
            session = session_service.create_session()
            session_service.session_dict[session.session_id] = session
    llm_response = tutor_service.handle_submission(request.body, session=session)
    print(llm_response)
    json_response = {
        "session_id": request.session_id,
        "intent": llm_response[0],
        "response": llm_response[2],
    }
    return json_response
