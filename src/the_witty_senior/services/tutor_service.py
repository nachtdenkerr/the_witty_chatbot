"""
Tutor service
"""
import os
from openai import OpenAI
from dotenv import load_dotenv
from the_witty_senior.services.llm_service import QuestionStrategy, HintStratergy, AnalogyStrategy, ExplanationStrategy, CongratsStratery, RedirectStratery, get_llm_response

def handle_submission(request):
    """
    Decide response trategy
    """
    intent=["information_request", "confused", "partially_understand", "needs_example", "mostly_correct"]
    model="gpt-5.5"
    load_dotenv(os.path.join(os.getcwd(), ".env"))
    client = OpenAI()
    intent_response = client.responses.create(
        model=model,
        reasoning={"effort": "medium"},
        instructions="""You are an intent classifier.
                        Allowed intents:
                        - information_request
                        - confused
                        - partially_understand
                        - needs_example
                        - mostly_correct
                        - out_of_scope

                        Return ONLY one intent.
                        "with confidence value in the range 0 to 1.""",
        input=request,
    )
    user_intent = intent_response.output_text
    print(user_intent)
    if intent[0] in user_intent:
        strategy = ExplanationStrategy()
    elif intent[1] in user_intent:
        strategy = QuestionStrategy()
    elif intent[2] in user_intent:
        strategy = HintStratergy()
    elif intent[3] in user_intent:
        strategy = AnalogyStrategy()
    elif intent[4] in user_intent:
        strategy = CongratsStratery()
    else:
        strategy = RedirectStratery()
    return user_intent, strategy.__class__(), get_llm_response(client=client, request=request, model=model, strategy=strategy)
