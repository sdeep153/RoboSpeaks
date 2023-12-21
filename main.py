import pyttsx3 as py

if __name__ == '__main__':
    engine = py.init()

    while True:
        text = input('Enter the text to speak: ')
        if text == 'quit':
            break
        engine.say(text)
        engine.runAndWait()

    pass
