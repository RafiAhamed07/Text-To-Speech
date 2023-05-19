# import os
import pyttsx3

engine = pyttsx3.init()
if __name__ == '__main__':
    print("Welcome to RoboSpeaker1.0 , Created by Fida")
    while True:
        x = input("Enter what you want to speak: ")
        # if x == 'quit':
        #     a = "Bye bye"
        #     engine.say(a)
        #     break
        engine.say(x)
        engine.runAndWait()