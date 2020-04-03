

from tkinter import *




class StartGUI():

    def __init__(self, StartWindow1, Player1, Math1):
        StartWindow = StartWindow1
        Player = Player1
        Math = Math1
        

        StartWindow.title("Start New Game")
        #StartWindow.minsize(250,100)


        StartWindow.Name = StringVar()
        StartWindow.Age = StringVar()
        StartWindow.Difficulty = StringVar()
        StartWindow.MyLabel = StringVar()

        StartWindow.Name.set(Player.Name)
        StartWindow.Age.set(Player.Age)

        StartWindow.Difficulty.set(Math.Difficulty)



        # define what happens when you click submit
        def SubmitClick():
            if NameEntry.get() == "" or AgeEntry.get() =="":
                StartWindow.MyLabel.set("enter values for name and age")
            else:
                Player.Start = TRUE
                Player.Name = NameEntry.get()
                Player.Age = AgeEntry.get()
                Math.Difficulty= StartWindow.Difficulty.get()
                StartWindow1.destroy()



        # create the label objects
        NameLabel = Label(StartWindow, text="Name", anchor=W, width=10)
        AgeLabel = Label(StartWindow, text="Age", anchor=W, width=10)
        DifficultyLabel = Label(StartWindow, text="Difficulty", anchor=W, width=10)
        OutputLabel = Label(StartWindow, textvariable=StartWindow.MyLabel)

        # create the text entry objects
        NameEntry = Entry(StartWindow, textvariable = StartWindow.Name, width=20)
        AgeEntry = Entry(StartWindow, textvariable = StartWindow.Age, width=20)

        # create the difficutly radio buttons
        EasyButton = Radiobutton(StartWindow, text="Easy", variable=StartWindow.Difficulty,  value="E")
        MediumButton = Radiobutton(StartWindow, text="Medium", variable=StartWindow.Difficulty, value="M")
        HardButton = Radiobutton(StartWindow, text="Hard", variable=StartWindow.Difficulty, value="H")
        

        # create the button objects
        SubmitButton = Button(StartWindow, text="submit", command=SubmitClick)


        # place the objects in the window grid
        NameLabel.grid(row=0, column=0)
        NameEntry.grid(row=0, column=1)
        SubmitButton.grid(row=0, column=2, padx=10, pady=5)
        AgeLabel.grid(row=1, column=0)
        AgeEntry.grid(row=1, column=1)
        DifficultyLabel.grid(row=2, column=0)
        EasyButton.grid(row=3, column=0)
        MediumButton.grid(row=4, column=0)
        HardButton.grid(row=5, column=0)
        OutputLabel.grid(row=6, columnspan=3, pady=20)




class GUI():
    
    def __init__(self, MainWindow1, Math1, Player1):

        # receive the Tkinter object and assign it an attribute of this class
        # give the main window a title
        # set the minimum size of the main window
        MainWindow = MainWindow1
        Math = Math1
        Player = Player1
        MainWindow.title("Main Window")
        #MainWindow.minsize(450,150)


        MainWindow.Name = StringVar()
        MainWindow.Age = StringVar()
        MainWindow.Difficulty = StringVar()

        MainWindow.Name.set(Player.Name)
        MainWindow.Age.set(Player.Age)
        MainWindow.Difficulty.set(Math.Difficulty)

        MainWindow.MyLabel = StringVar()



        # define what happens when you click submit
        def SubmitClick():
            pass


        # define what happends when you click clear
        def ClearClick():
            MainWindow.Name.set("")
            MainWindow.Age.set("")
            MainWindow.MyLabel.set("")


        # create the label objects
        NameLabel = Label(MainWindow, text="Name", anchor=W, width=10)
        AgeLabel = Label(MainWindow, text="Age", anchor=W, width=10)
        DifficultyLabel = Label(MainWindow, text="Difficulty", anchor=W, width=10)

        OutputLabel = Label(MainWindow, textvariable=MainWindow.MyLabel)
        

        # create the text entry objects
        PlayerName = Label(MainWindow, anchor=W, textvariable = MainWindow.Name)
        PlayerAge = Label(MainWindow, anchor=W, textvariable = MainWindow.Age)
        GameDifficulty = Label(MainWindow, anchor=W, textvariable = MainWindow.Difficulty)
        

        # create the button objects
        SubmitButton = Button(MainWindow, text="submit", command=SubmitClick)
        ClearButton = Button(MainWindow, text="clear", command=ClearClick)
        OtherButton = Button(MainWindow, text="other", command=Math.MathFun)


        # place the objects in the window grid
        NameLabel.grid(row=0, column=0)
        AgeLabel.grid(row=1, column=0)
        PlayerName.grid(row=0, column=1)
        PlayerAge.grid(row=1, column=1)
        DifficultyLabel.grid(row=2, column=0)
        GameDifficulty.grid(row=2, column=1)
        SubmitButton.grid(row=0, column=3, padx=10, pady=5)
        ClearButton.grid(row=1, column=3, padx=10, pady=5)
        OtherButton.grid(row=2, column=3, padx=10, pady=5)
        OutputLabel.grid(row=3, columnspan=3, pady=20)


class GamePlayer():

    def __init__(self):
        self.Name = ""
        self.Age = ""
        self.Start = FALSE



class DoMath():

    def __init__(self):
        self.name = "Game Name"
        self.Difficulty = "E"


    def MathFun(self):
        if self.name =="Game Name":
            self.name = "You changed the name"
        else:
            self.name = "Game Name"


# Create the Tkinter object and pass it to the GUI class
# Create the Math object and pass it to the GUI class

Player1 = GamePlayer()
Math1 = DoMath()
StartWindow1 = Tk()

myStartGUI = StartGUI(StartWindow1, Player1, Math1)
StartWindow1.mainloop()

if Player1.Start == TRUE:
    
    MainWindow1 = Tk()
    myGUI = GUI(MainWindow1,Math1,Player1)
    MainWindow1.mainloop()
