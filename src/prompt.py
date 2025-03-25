
def get_question_flashcard_prompt(user_group: str, topic: str) -> str:
    """Prompt for question flashcards. The front is the question, and the back is the answer."""
    return f"""
        Generate 10 fun and engaging flashcards for {user_group} on the topic of {topic}.
        The output should be a JSON list of dictionaries, where each dictionary has 'front' and 'back' keys.
        The front contains common questions, the back contains the answer, with cute characters.
        Example:
        ```json
        [
            {{"front": "The king of the jungle who loves to ROAR!", "back": "Lion"}},
            {{"front": "A happy waddler from the icy lands who can't fly!", "back": "Penguin"}}
        ]
    """

def get_japanese_flashcard_prompt() -> str:
    """Specific prompt for Japanese flashcards."""
    return f"""
        Generate 10 flashcards for Japanese learners.
        The output should be a JSON list of dictionaries, where each dictionary has 'front' and 'back' keys.
        The front contains common English words or phrases, the back contains the translated Japanese in both Romaji and Kanji.
        Example:
        ```json
        [
            {{"front": "dog", "back": "inu"}},
            {{"front": "Welcome home", "back": "Okaerinasai"}},
            {{"front": "Nice to meet you.", "back": "Hajimemashite"}}
        ]
    """