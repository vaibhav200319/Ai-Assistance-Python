import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        print("🎙️ Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            speak("Mic timeout, please try again.")
            return ""
    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        speak("Internet connection problem.")
    return ""

def write_code(code):
    with open("output_code.py", "a") as f:
        f.write(code + "\n")

if __name__ == "__main__":
    speak("Hello Sir! I am your assistant.")
    while True:
        command = take_command()

        if command == "":
            continue

        if "for loop" in command:
            code = "for i in range(10):\n    print(i)"
            speak("Here's a for loop.")
            print(code)
            write_code(code)

        elif "function" in command:
            code = "def greet():\n    print('Hello!')"
            speak("Here's a Python function.")
            print(code)
            write_code(code)

        elif "if condition" in command:
            code = "if x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')"
            speak("Here is an if-else condition.")
            print(code)
            write_code(code)

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "chat gpt" in command or "chatgpt" in command or "openai" in command:
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("Command not recognized. Try again.")
