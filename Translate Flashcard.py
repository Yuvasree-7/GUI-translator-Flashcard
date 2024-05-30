#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import tkinter as tk
import random
from gtts import gTTS
import os
from googletrans import Translator

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("English-Tamil Flashcards")

        # Vocabulary data (English words and their Tamil translations)
        self.vocab = {}
        self.get_user_input()

        self.current_pair = None
        self.create_widgets()

    def get_user_input(self):
        # Get the number of word pairs the user wants to input
        num_pairs = int(input("Enter the number of word pairs you want to input: "))

        # Get user input for each word pair
        for _ in range(num_pairs):
            english_word = input("Enter an English word: ")
            tamil_translation = self.translate_to_tamil(english_word)
            self.vocab[english_word] = tamil_translation

    def translate_to_tamil(self, english_word):
        try:
            translator = Translator()
            translation = translator.translate(english_word, dest='ta')
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return "Translation not available"

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=200, bg="blue")  # Set background color to blue
        self.canvas.pack(pady=20)

        self.next_card()

        self.btn_play_english_audio = tk.Button(self.master, text="Play English Pronunciation", command=self.play_english_audio)
        self.btn_play_english_audio.pack(pady=5)

        self.btn_play_tamil_audio = tk.Button(self.master, text="Play Tamil Pronunciation", command=self.play_tamil_audio)
        self.btn_play_tamil_audio.pack(pady=5)

        self.btn_next_card = tk.Button(self.master, text="Next Card", command=self.next_card)
        self.btn_next_card.pack(pady=10)

    def next_card(self):
        self.current_pair = random.choice(list(self.vocab.items()))
        self.show_flashcard()

    def show_flashcard(self):
        self.show_word()

    def show_word(self):
        self.canvas.delete("all")
        english_word, tamil_translation = self.current_pair
        display_text = f"{english_word}\n({tamil_translation})"
        self.canvas.create_text(200, 100, text=display_text, font=("Helvetica", 14), fill="white")  # Set text color to white

    def play_english_audio(self):
        if self.current_pair:
            english_word, _ = self.current_pair
            generate_audio_spelling(english_word, language='en')

    def play_tamil_audio(self):
        if self.current_pair:
            _, tamil_translation = self.current_pair
            generate_audio_spelling(tamil_translation, language='ta')

def generate_audio_spelling(word, language='en'):
    try:
        # Generate TTS audio for the given word and language
        tts = gTTS(text=word, lang=language, slow=False)

        # Save the audio file
        audio_path = f"{word}.mp3"
        tts.save(audio_path)

        # Play the audio file
        os.system(f"start {audio_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




