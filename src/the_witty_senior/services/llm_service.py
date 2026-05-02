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

def get_llm_response(client, request, model, strategy):
    """
    Get LLM response with pre-defined response strategy
    """
    response = client.responses.create(
        model=model,
        reasoning=strategy.reasoning,
        instructions=strategy.instructions,
        input=request
    )
    return response.output_text
