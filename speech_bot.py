import speech_recognition as sr
import openai
import pyttsx3
from transformers import pipeline
import tkinter as tk
from threading import Thread

openai.api_key = "My_APi_Key"
# Speech Recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("API unavailable")

# GPT-3 or GPT-2 (if using local model) Response Generation
import openai

openai.api_key =  "My_Api_Key" # Replace with your OpenAI API key
def generate_response(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

    # Alternatively for GPT-2 (local model):
    # generator = pipeline('text-generation', model='gpt2')
    # response = generator(prompt, max_length=150, num_return_sequences=1)
    # return response[0]['generated_text']

# Text-to-Speech function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main Bot Function to handle speech input and output
def speech_to_speech_bot():
    while True:
        user_input = recognize_speech()
        if user_input:
            bot_response = generate_response(user_input)
            print(f"Bot: {bot_response}")
            speak(bot_response)

# Optional GUI using Tkinter
def start_bot():
    bot_thread = Thread(target=speech_to_speech_bot)
    bot_thread.start()

# Creating a basic GUI with Tkinter
root = tk.Tk()
root.title("Speech-to-Speech Bot")

start_button = tk.Button(root, text="Start", command=start_bot)
start_button.pack()

root.mainloop()
