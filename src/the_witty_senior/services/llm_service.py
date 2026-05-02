"""
Defined interactions with LLM
"""

from openai import OpenAI
from dotenv import load_dotenv
import os
import random
import the_witty_senior.core.config as config

load_dotenv(os.path.join(os.getcwd(), ".env"))

client = OpenAI()

class QuestionStrategy():
    def __init__(self):
        self.instructions="Asking clarifying questions to know user understanding."
        self.reasoning={"effort": "high"}

class HintStratergy():
    def __init__(self):
        self.instructions="Response with maximum 4 hints. " \
    "Mention that the user can figure things out if he tries harder."
        self.reasoning={"effort": "medium"}
        self.tone="humor"

class AnalogyStrategy():
    def __init__(self):
        self.instructions="Give a humorous example."
        self.reasoning={"effort": "medium"}

class ExplanationStrategy():
    def __init__(self):
        self.instructions="You gather information an use simple terms to explain the concept in one sentence. " \
        "Then ask the user whether they need a small example."
        self.reasoning={"effort": "medium"}

class CongratsStratery():
    def __init__(self):
        self.instructions="Response with a cheerful congratulation in 1 sentence."
        self.reasoning={"effort": "low"}

class RedirectStratery():
    def __init__(self):
        self.instructions="Apologize for not understanding the request. " \
        "Asking the user to reinput his prompt that is related to the learning topic."
        self.reasoning={"effort": "low"}

def get_user_intent(request):
    """
    Use AI to generate the user intent
    """
    if config.LLM_MOCK_ENABLED:
        intent_mode = random.choice(list(range(5)))
        return config.intent[intent_mode]

    intent_response = client.responses.create(
        model=config.OPENAI_MODEL,
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
    return intent_response.output_text

def get_llm_response(history, request, strategy):
    """
    Get LLM response with pre-defined response strategy based on user intent
    """
    if config.LLM_MOCK_ENABLED:
        if strategy is QuestionStrategy:
            response = "What exactly do you know about the topic?"
        elif strategy is AnalogyStrategy:
            response =  "Think of it like the two goat story."
        elif strategy is CongratsStratery:
            response =  "See, I know you can do it."
        elif strategy is RedirectStratery:
            response =  "I do not think that is related to our learning topic."
        elif strategy is ExplanationStrategy:
            response =  "I have no idea what you are talking about."
        elif strategy is HintStratergy:
            response =  "Maybe check Google for 5 minutes then return."
        else:
            response = "SOS"
        return response

    response = client.responses.create(
        model=config.OPENAI_MODEL,
        reasoning=strategy.reasoning,
        instructions=strategy.instructions,
        input=history + " " + request
    )
    return response.output_text

def get_session_summary(session_history):
    """
    Summarise session history to reduce tokens used for chat with history.
    """
    if config.LLM_MOCK_ENABLED:
        return "They have done this and that and that and this."
    response = client.responses.create(
        model=config.OPENAI_MODEL,
        reasoning="high",
        instructions="Summarize learning state of the user into maximum 5 bullet points." \
        "If there are several topics, prioritize the one they do not had a good understanding yet.",
        input=session_history)
    return response.output_text
