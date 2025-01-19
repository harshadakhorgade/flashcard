# Flashcards Language Learning Application

This Python application helps users learn new words in a foreign language using a flashcard-based approach. It randomly displays words in the target language, allowing users to guess the meaning before revealing the translation. Users can mark words as learned, which are then removed from the future study list.

## Features
- Flashcard-based learning with translations between two languages.
- Automatically saves progress, so users only study unlearned words.
- Simple and interactive GUI built using Tkinter.
- Stores data in CSV format for easy management.

## Prerequisites
- Python 3.x
- Pandas library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/harshadakhorgade/flashcard.git
   cd flashcards-app
   ```

2. Install dependencies:
   ```bash
   pip install pandas
   ```

3. Ensure the following directory structure exists:
   ```plaintext
   data/
       french_words.csv
       to_learn.csv
   images/
       card_front.png
       card_back.png
       right.png
       wrong.png
   ```

## Configuration
1. **Data Files:**
   - `french_words.csv`: The original dataset containing words in French and their English translations.
   - `to_learn.csv`: Tracks unlearned words. This file is created automatically when the program runs for the first time.

2. **Images:**
   - `card_front.png` and `card_back.png`: Background images for the flashcards.
   - `right.png` and `wrong.png`: Icons for the "Known" and "Unknown" buttons.

## Usage
1. Run the application:
   ```bash
   python main.py
   ```

2. The GUI will display a French word:
   - After 3 seconds, the flashcard flips to reveal the English translation.

3. Use the buttons:
   - Click the **checkmark** (right.png) button if you know the word.
   - Click the **cross** (wrong.png) button if you don’t know the word.

4. Words marked as known are removed from the future study list, and the updated list is saved to `to_learn.csv`.

## Code Explanation

### Main Functions
#### `next_card()`
- Randomly selects a new word from the `to_learn` list and displays it on the flashcard.
- Resets the timer for flipping the card.

#### `flip_card()`
- Flips the flashcard to show the English translation of the current word.

#### `is_known()`
- Removes the current word from the `to_learn` list.
- Updates `to_learn.csv` to save progress.
- Displays the next card.

### User Interface
- The GUI is built using Tkinter.
- A `Canvas` widget displays the flashcard and text.
- Two `Button` widgets handle user interactions (“Known” and “Unknown”).

### File Handling
- `french_words.csv` is loaded initially to populate the flashcards.
- Progress is saved to `to_learn.csv` whenever a word is marked as known.
- If `to_learn.csv` exists, it is loaded instead of `french_words.csv`.

## Notes
- Ensure the `images` and `data` directories exist and contain the necessary files.
- Customize the `french_words.csv` file to include your preferred languages.

## License
This project is licensed under the MIT License. Feel free to use and modify it.

