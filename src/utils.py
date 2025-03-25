import os
import json
import openai
import random
import streamlit as st
from prompt import get_question_flashcard_prompt, get_japanese_flashcard_prompt
from src.constant import (
    MATH, SCIENCE, ANIMAL, SAFARI_ANIMAL, OCEAN_ANIMAL, FRUIT_AND_FOOD, JAPANESE
)

def generate_flashcards(user_group: str, topic: str) -> list[dict]:
    """
    Generate flashcards.
    """
    if topic in [MATH, SCIENCE, ANIMAL, SAFARI_ANIMAL, OCEAN_ANIMAL, FRUIT_AND_FOOD]:
        prompt = get_question_flashcard_prompt(user_group, topic)
    elif topic in [JAPANESE]:
        prompt = get_japanese_flashcard_prompt()
    else:
        raise ValueError("Unknown topic identified!")
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a flashcard generator that creates fun and engaging cards for kids."},
                  {"role": "user", "content": prompt}],
        temperature=1,
    )
    flashcards_str = response.choices[0].message.content.strip()
    flashcards_str = flashcards_str.replace("```json\n", "").replace("\n```", "").strip()
    try:
        flashcards = json.loads(flashcards_str)
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON. Check LLM output.\n{flashcards_str}")
        flashcards = []

    return [card for card in flashcards if len(card) == 2]


def save_flashcards(flashcards: list[str], topic: str) -> None:
    """Function to save flashcards."""
    filedir = f"data/{topic}"
    if not os.path.exists(filedir):
        os.makedirs(filedir)
    filename = random.getrandbits(128)
    filepath = f"{filedir}/{filename}.json"

    with open(filepath, "w") as f:
        json.dump(flashcards, f)


def load_flashcards(uploaded_file: str) -> list[dict]:
    """Function to load flashcards"""
    return json.load(uploaded_file)


def flip_card(is_flipped: bool) -> bool:
    """Flip the card."""
    return not is_flipped


def reset_session_state() -> None:
    """Function to reset session state."""
    st.session_state["flashcards"] = []
    st.session_state["current_index"] = 0
    st.session_state["flipped"] = False