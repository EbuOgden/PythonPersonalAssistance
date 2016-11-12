import wikipedia
import wolframalpha
from Tkinter import *

class MainGUI():
    def __init__(self):
        self.mainGUI = Tk()
        self.mainGUI.title("Personal Assistant")
        self.mainGUI.resizable(width=True, height=True)
        self.mainGUI.geometry('500x200')

        self.introLabel = Label(self.mainGUI, text="Welcome to your personal assistant. You can ask any mathematical formula or any title. How can I help you?", wraplength=500) # INTRO MESSAGE
        self.introLabel.pack()

        self.questionLabel = Label(self.mainGUI, text="Please ask a question : ") # QUESTION_MESSAGE
        self.questionLabel.pack( side = LEFT)

        self.questionInput = Entry(self.mainGUI) # QUESTION_
        self.questionInput.pack( side = LEFT)

        self.answerButton = Button(self.mainGUI, text="Find my path!", command=self.findMyAnswer) # ANSWER_BUTTON
        self.answerButton.pack( side = LEFT)

        self.mainGUI.mainloop()

    def findMyAnswer(self):
        input = self.questionInput.get()
        try:
            #wolframalpha
            wolframalpha_appId = "*********" # 

            client = wolframalpha.Client(wolframalpha_appId) # using app id for WolframAlpha API
            res = client.query(input)
            answer = next(res.results).text

            answerWindow = Toplevel(self.mainGUI) # NEW_WINDOW
            answerWindow.geometry('600x400')
            answerWindow.title("Result")

            answerText = Text(answerWindow) # ANSWER_MESSAGE
            answerText.insert(INSERT, input + ", Answer is : " + answer)
            answerText.pack()

        except:
            #wikipedia
            answer = wikipedia.summary(input)
            answerWindow = Toplevel(self.mainGUI) # NEW_WINDOW

            answerWindow.geometry('600x400')
            answerWindow.title("Result")

            answerText = Text(answerWindow) # ANSWER_MESSAGE
            answerText.insert(INSERT, input + ", Answer is : " + answer)
            answerText.pack()

            #answerlabel = Label(answerWindow, text=answer, justify=LEFT, wraplength=500) # ANSWER_MESSAGE
            #answerlabel.pack()

if __name__ == "__main__":
        MainGUI()
