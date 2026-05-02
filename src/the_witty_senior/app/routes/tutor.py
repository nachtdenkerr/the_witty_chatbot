"""
Module docstring
"""

import json
from fastapi import APIRouter
from the_witty_senior.services import tutor_service
from the_witty_senior.models.attempt import RequestSubmission

router = APIRouter()

@router.post("/tutor")
def tutoring(request: RequestSubmission):
    """
    Submit endpoint that will run and evaluate the code submission from user
    """
    print(request)
    llm_response = tutor_service.handle_submission(request.body)
    print(llm_response)
    json_response = {
        "intent": llm_response[0],
        "response": llm_response[2],
    }
    return json.dumps(json_response)
