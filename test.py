import pyttsx3
import speech_recognition as sr
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the gpt2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
num_return_sequences = 1

def generate_response(input_ids, max_length=100, num_return_sequences=1, temperature=0.7):
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        temperature=temperature,
        top_k=50,  # Consider top-50 tokens during sampling
        top_p=0.95,  # Use nucleus sampling with cumulative probability cutoff
        repetition_penalty=1.2,  # Discourage repetition in generated sequences
        no_repeat_ngram_size=3,  # Avoid repeating n-grams of size 3
        early_stopping=True  # Stop generation when EOS token is reached
    )
    return output

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech using Google Speech Recognition
def listen_continuous():
    global listening
    while listening:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {query}\n")
            process_command(query)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass

# Function to perform actions based on voice commands
def process_command(command):
    command = command.lower()
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "who are you" in command:
        speak("I am your super intelligent AI assistant!")
    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(results)
    elif "open" in command:
        website = command.replace("open", "")
        speak(f"Opening {website}")
        webbrowser.open(f"https://www.{website.strip()}.com")
    elif "launch" in command:
        app_name = command.replace("launch", "").strip()
        speak(f"Launching {app_name}")
        try:
            os.system(f"start {app_name}")
        except Exception as e:
            speak(f"Error launching {app_name}: {str(e)}")
    elif "run" in command:
        app_name = command.replace("run", "").strip()
        speak(f"Launching {app_name}")
        os.system(f"python Gesture_Controller.py")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        listening = False
    else:
        input_ids = tokenizer.encode(command, return_tensors="pt")
        response = generate_response(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
        response_text = tokenizer.decode(response[0], skip_special_tokens=True)
        speak(response_text)
        
# Start continuous listening
listening = True
listen_continuous()
