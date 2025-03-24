import streamlit as st
import os
import openai
import json
import random
from flashprompt import get_question_flashcard_prompt, get_japanese_flashcard_prompt

# Function to call GPT-4o for flashcard generation
def generate_flashcards(user_group, topic):
    if topic in ["Animal Flashcards", "Math Questions", "Science Trivia", 
                 "Safari Animals", "Ocean Animals", "Pet Animals"]:
        prompt = get_question_flashcard_prompt(user_group, topic)
    elif topic in ["Japanese Flashcards"]:
        prompt = get_japanese_flashcard_prompt(topic)
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

# Function to save flashcards
def save_flashcards(flashcards, topic):
    filedir = f"data/{topic}"
    if not os.path.exists(filedir):
        os.makedirs(filedir)
    filename = random.getrandbits(128)
    filepath = f"{filedir}/{filename}.json"
        

    with open(filepath, "w") as f:
        json.dump(flashcards, f)

# Function to load flashcards
def load_flashcards(uploaded_file):
    return json.load(uploaded_file)

# Function to handle card flipping
def flip_card(is_flipped):
    return not is_flipped

# Function to reset session state
def reset_session_state():
    st.session_state["flashcards"] = []
    st.session_state["current_index"] = 0
    st.session_state["flipped"] = False

# Streamlit UI with Kids-Friendly Design
st.set_page_config(page_title="Fun Flashcard Creator", page_icon="📚", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎨 Fun Flashcard Creator 🎈</h1>", unsafe_allow_html=True)

# User Selection
st.markdown("<h3 style='color: #FFA500;'>📌 Select Your Preferences</h3>", unsafe_allow_html=True)
user_group = st.selectbox("Select User Group:", ["Pre-K to Grade 1", "Grade 2 to Grade 3", "Grade 4 and above"], index=0)
topic = st.selectbox("Select Flashcard Type:", [
    "Japanese Flashcards", "Animal Flashcards", "Math Questions", "Science Trivia",
    "Safari Animals", "Ocean Animals", "Pet Animals",
], index=0)

# Refresh Button
if st.button("🔄 Refresh"):
    reset_session_state()
    st.rerun()

if st.button("🎨 Generate Flashcards 🎈"):
    flashcards = generate_flashcards(user_group, topic)
    st.session_state["flashcards"] = flashcards
    st.session_state["current_index"] = 0


# File Upload for Loading Flashcards
st.markdown("<h3 style='color: #FFA500;'>📂 Upload Saved Flashcards</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Saved Flashcards", type=["json"])
if uploaded_file is not None and not st.session_state.get("flashcards"):
    st.session_state["flashcards"] = load_flashcards(uploaded_file)
    st.session_state["current_index"] = 0

# Ensure session state variables exist
if "flashcards" not in st.session_state:
    st.session_state["flashcards"] = []
if "current_index" not in st.session_state:
    st.session_state["current_index"] = 0
if "flipped" not in st.session_state:
    st.session_state["flipped"] = False

# Cache the flashcards and current index
# @st.cache_data
def get_state():
    return st.session_state["flashcards"], st.session_state["current_index"]

# Load the state
flashcards, current_index = get_state()

if flashcards:
    if 0 <= current_index < len(flashcards):
        card = flashcards[current_index]
        front = card["front"]
        back = card["back"]

        # Flashcard UI
        st.markdown("<h3 style='color: #FF69B4;'>📖 Flashcard</h3>", unsafe_allow_html=True)

        flipped = st.button("🔄 Flip Card")  # Button to trigger the flip
        if flipped:
            st.session_state["flipped"] = flip_card(st.session_state["flipped"])

        if st.session_state["flipped"]:
            card_container = st.container()
            card_container.markdown(f"<div style='padding: 20px; background-color: #FFFF99; border-radius: 10px; text-align: center; font-size: 24px;'>🃏 {back}</div>", unsafe_allow_html=True)
        else:
            card_container = st.container()
            card_container.markdown(f"<div style='padding: 20px; background-color: #ADD8E6; border-radius: 10px; text-align: center; font-size: 24px;'>📖 {front}</div>", unsafe_allow_html=True)

        # Navigation
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("⬅️ Previous") and current_index > 0:
                st.session_state["current_index"] -= 1
                st.session_state["flipped"] = False
                st.rerun()  # Force a rerun to update the display
        with col2:
            if st.button("➡️ Next") and current_index < len(flashcards) - 1:
                st.session_state["current_index"] += 1
                st.session_state["flipped"] = False
                st.rerun()  # Force a rerun to update the display
        with col3:
            if st.button("💾 Save Flashcards"):
                save_flashcards(flashcards, topic)
                st.success("Flashcards saved successfully! 🎉")


# Adding fun decorations
st.markdown("""
    <style>
        div.stButton > button {
            background-color: #FF69B4;
            color: white;
            border-radius: 10px;
            font-size: 20px;
            padding: 10px;
        }
        div.stButton > button:hover {
            background-color: #FF1493;
        }
    </style>
    """, unsafe_allow_html=True)