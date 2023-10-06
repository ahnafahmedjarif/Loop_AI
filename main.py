import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os

loop_engine = pyttsx3.init("sapi5") #
loop_voices = loop_engine.getProperty('voices')
# print(voices[1].id)
loop_engine.setProperty('voice', loop_voices[1].id) # Set the voice into the engine


user_name = input("Whats your name ? ")
user_gender = input('Whats your gender ? Male or Female : ')
def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(f"Good Morning {user_name} ")
    elif hour >= 12 and hour <=18:
        speak(f"Good Afternoon  {user_name} ")
    else:
        speak(f'Good Evening{user_name}')

    if user_gender == "male":
        speak(" I am loop. How can i assist you sir ? ")
    elif user_gender == "female":
        speak("I am loop. How can i assist you mam ?")
    else:
        print('Invalid gender !')

def user_command():
    #It takes microphone input from user and returns string output
    audio_recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        print("Analyzing your command......")
        audio_recognizer.pause_threshold = 1
        audio_recognizer.energy_threshold = 500
        audio = audio_recognizer.listen(source)
    try:
        print("Recognizing....")
        user_command_deliver = audio_recognizer.recognize_google(audio , language="en-in")
        print(f"{user_name} : {user_command_deliver}\n")

    except Exception as e:
        print("Couldn't understand. Please say again !")
        return "None"
    return user_command_deliver



def speak(audio):
    loop_engine.say(audio)
    loop_engine.runAndWait()

if __name__ == "__main__":
    # speak("jarif is a good boy")
    wish_me()
    while True:
        user_command_deliver = user_command().lower()
        if 'wikipedia' in user_command_deliver:
            speak('Searcing wikipedia...')
            result =  wikipedia.summary(user_command_deliver , sentences = 2)
            speak(f"From wikipedia")
            print(result)
            speak(result)

