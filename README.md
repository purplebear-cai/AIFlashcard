# Flashcard Generator with Streamlit

This project is a **flashcard generator** built with **Python and Streamlit**, allowing users to create customized flashcards for learning in an interactive and user-friendly way.

## Features

- **User Selection**: Choose user group (e.g., Pre-K to Grade 1, Grade 2 to Grade 3, etc.) and topic (e.g., word flashcards, question flashcards).
- **AI-Generated Flashcards**: Uses GPT-4o to generate 10 flashcards based on user input.
- **Interactive Flashcards**:
  - Each flashcard has a **front** and **back** side.
  - Click on the card to **flip** between sides.
  - Navigate between flashcards using **Next** and **Previous** buttons.
- **Save & Upload**:
  - Users can **save** generated flashcards.
  - Previously saved flashcards can be **uploaded** for reuse.
- **Kid-Friendly UI**: A fun and engaging design that makes learning enjoyable for children.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/purplebear-cai/AIFlashcard.git
   cd AIFlashcard
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment:
   To run the repository, you need to set up your OpenAI API key, and save it in the .env file.
   ```
   OPENAI_API_KEY={Your_OpenAI_API_key}
   ```

   Set up your PYTHONPATH:
   ```sh
   export PYTHONPATH={Folder_to_AIFlashcard}
   ```

4. Run the Streamlit app:
   ```sh
   streamlit run src/app.py
   ```

## Usage
1. Select user group and topic.
2. Click Generate Flashcards to create a set of 10 flashcards.
3. Click a flashcard to flip between front and back.
4. Use Next/Previous buttons to navigate.
5. Click Save to store flashcards locally.
6. Upload a previously saved file to load flashcards again.
7. Do not forget to click **Refresh** if you want to reupload or regenearte new flashcards