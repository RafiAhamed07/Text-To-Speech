from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to speech")
root.geometry("524x250")
root.maxsize(524, 250)
root.minsize(524, 250)


def say():
    engine = pyttsx3.init()
    if __name__ == '__main__':
        print("Welcome to RoboSpeaker1.0 , Created by Fida")
        # while True:
        x = textvalue.get()
        # if x == 'quit':
        #     a = "Bye bye"
        #     engine.say(a)
        #     break
        engine.say(x)
        engine.runAndWait()


def reset():
    textvalue = StringVar(root)
    textvalue.set("")
    textentry.config(textvariable=textvalue)


# var = StringVar(root)
# var.set("")

# Heading
Label(root, text="Welcome to RoboSpeaker", font="comicsnasms 13 bold", pady=15, padx=150).grid(row=0, column=3)

# txt for Ask
text = Label(root, text="Plaease Type your text", pady=10)

# yake txt input
text.grid(row=1, column=3)

textvalue = StringVar(root)

textvalue.set("")

# Entry for our input
textentry = Entry(root, textvariable=textvalue)

# pack the entries
textentry.grid(row=2, column=3, pady=5)

# botton & packing it and asdsinging it a command

Button(text="Say", command=say).grid(row=3, column=3, pady=5)
# Button(text="Reset", command=reset).grid(row=4, column=3, pady=5)

root.mainloop()
