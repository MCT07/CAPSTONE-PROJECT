
def validate_output(response):

    if not response.strip():
        return False

    return True


def guardrails_check(response):

    banned_words = [
        "hack",
        "illegal",
        "attack",
        "bypass"
    ]

    for word in banned_words:

        if word in response.lower():
            return False

    return True
