"""
Tutor service
"""

import the_witty_senior.services.llm_service as llm_service
import the_witty_senior.services.session_service as session_service
import the_witty_senior.core.config as config

def handle_submission(request, session):
    """
    Decide response trategy
    """

    user_intent = llm_service.get_user_intent(request=request)

    if config.intent[0] == user_intent:
        strategy = llm_service.ExplanationStrategy()
    elif config.intent[1] == user_intent:
        strategy = llm_service.QuestionStrategy()
    elif config.intent[2] == user_intent:
        strategy = llm_service.HintStratergy()
    elif config.intent[3] == user_intent:
        strategy = llm_service.AnalogyStrategy()
    elif config.intent[4] == user_intent:
        strategy = llm_service.CongratsStratery()
    else:
        strategy = llm_service.RedirectStratery()

    llm_response = llm_service.get_llm_response(session.history, request, strategy)
    session_service.update_session(session, request, llm_response)

    return user_intent, strategy.__class__(), llm_response
