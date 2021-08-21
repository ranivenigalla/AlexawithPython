import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        print("error in listening")
    return command


def run_alexa():
    command = take_command()
    print(command)
    greet=["hi","hello","hey","hola"]
    if any(greetings in command for greetings in greet):
        tell=''
        if "how" in command:
            tell="I am fine ,Thanks for asking that. I hope Your fine too"
        else:
            tell=random.choice(greet)+"how are you?"
        talk(tell)
    elif 'fine' in command:
        talk("It's good to hear that your fine")
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info=wikipedia.summary(person)
        pos=info.find('.')

        print(info[:pos])
        talk(info[:pos])
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except:
        print("Some error")
        break

