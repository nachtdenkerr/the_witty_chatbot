"""
Module docstring
"""

from fastapi import APIRouter
from the_witty_senior.services import tutor_service
from the_witty_senior.models.attempt import CodeSubmission

router = APIRouter()

@router.post("/submit")
def submit_code(request: CodeSubmission):
    """
    Submit endpoint that will run and evaluate the code submission from user
    """
    return tutor_service.handle_submission(request)
