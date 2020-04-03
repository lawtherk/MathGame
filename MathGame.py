


from tkinter import *




MainWindow = Tk()
MainWindow.title("Main Window")
MainWindow.minsize(500,200)
MainWindow.maxsize(500,200)

MainWindow.ButtonClicks = 0

Output = StringVar()
Output.set("asdfasdfa")

MainFrame = Frame(MainWindow, bg="Blue")
MainFrame.pack(expand=TRUE, fill=BOTH)

TopFrame = Frame(MainFrame, bg="Gray", height=40)
TopFrame.pack(fill=X)

BottomFrame = Frame(MainFrame, bg="green")
BottomFrame.pack(expand=TRUE, fill=BOTH)

BottomLeftFrame = Frame(BottomFrame, bg="blue", width=100, height=160)
BottomLeftFrame.pack(side=LEFT, fill=BOTH, expand=TRUE)

BottomRightFrame = Frame(BottomFrame, bg="red", width=400, height=160)
BottomRightFrame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

def DoSomething():
    print("worked")
    MainWindow.ButtonClicks = MainWindow.ButtonClicks+1
    Output.set("you clicked the button {} time(s)".format(MainWindow.ButtonClicks))

DoSomethingButton = Button(BottomLeftFrame, text="Do Something", command=DoSomething)
DoSomethingButton.pack()

DoSomethingLabel = Label(BottomRightFrame, textvariable=Output)
DoSomethingLabel.pack()




MainWindow.mainloop()