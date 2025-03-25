import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Variables
questionBank = [
    "What would you most want to be remembered as?",
    "A Muggle confronts you and says they dont believe in magic. You...",
    "You find a lost item that could be valuable. What do you do?",
    "What type of magic interests you the most?",
    "If you had to pick one pet, which would it be?",
    "You have a big exam tomorrow. How do you prepare?",
    "What kind of friend do you value the most?",
    "You and your friends find a secret passage at Hogwarts. What do you do?",
]

answerBank = [
    [
        "Bold and Daring",
        "Kind and Fair",
        "Intelligent and Wise",
        "Powerful and Influential",
    ],
    [
        "Show off a little spell",
        "Politely explain",
        "Ask them why they think that",
        "Use their ignorance to your advantage",
    ],
    [
        "Try to find the owner",
        "Keep it safe while investigating",
        "Take it to a teacher",
        "Keep it for yourself",
    ],
    [
        "Charms and Hexes",
        "Healing and Protection Spells",
        "Flying and Adventure Magic",
        "Ancient and Arcane Knowledge",
    ],
    [
        "A fierce and loyal lion",
        "A friendly and dependable badger",
        "A wise and mysterious owl",
        "A sleek and cunning serpent",
    ],
    [
        "Study intensely",
        "Study with friends",
        "Skim the important parts",
        "Find a way to get an advantage",
    ],
    [
        "Brave and adventurous",
        "Loyal and caring",
        "Thoughtful and insightful",
        "Resourceful and ambitious",
    ],
    [
        "Enter immediately",
        "Investigate carefully",
        "Make sure everyone is safe",
        "See if it could be useful",
    ],
]

answerWeight = [
    [
        ("Gryffindor", 2, "Slytherin", 1),
        ("Hufflepuff", 2, "Gryffindor", 1),
        ("Ravenclaw", 2, "Hufflepuff", 1),
        ("Slytherin", 2, "Ravenclaw", 1),
    ],
    [
        ("Gryffindor", 2, "Slytherin", 1),
        ("Hufflepuff", 2, "Ravenclaw", 1),
        ("Ravenclaw", 2, "Hufflepuff", 1),
        ("Slytherin", 2, "Gryffindor", 1),
    ],
    [
        ("Hufflepuff", 2, "Gryffindor", 1),
        ("Ravenclaw", 2, "Hufflepuff", 1),
        ("Gryffindor", 2, "Ravenclaw", 1),
        ("Slytherin", 2, "Ravenclaw", 1),
    ],
    [
        ("Slytherin", 2, "Ravenclaw", 1),
        ("Hufflepuff", 2, "Gryffindor", 1),
        ("Gryffindor", 2, "Hufflepuff", 1),
        ("Ravenclaw", 2, "Slytherin", 1),
    ],
    [
        ("Gryffindor", 2, "Slytherin", 1),
        ("Hufflepuff", 2, "Ravenclaw", 1),
        ("Ravenclaw", 2, "Hufflepuff", 1),
        ("Slytherin", 2, "Gryffindor", 1),
    ],
    [
        ("Ravenclaw", 2, "Slytherin", 1),
        ("Hufflepuff", 2, "Gryffindor", 1),
        ("Gryffindor", 2, "Hufflepuff", 1),
        ("Slytherin", 2, "Ravenclaw", 1),
    ],
    [
        ("Gryffindor", 2, "Hufflepuff", 1),
        ("Hufflepuff", 2, "Gryffindor", 1),
        ("Ravenclaw", 2, "Hufflepuff", 1),
        ("Slytherin", 2, "Ravenclaw", 1),
    ],
    [
        ("Gryffindor", 2, "Hufflepuff", 1),
        ("Ravenclaw", 2, "Slytherin", 1),
        ("Hufflepuff", 2, "Gryffindor", 1),
        ("Slytherin", 2, "Ravenclaw", 1),
    ],
]

houses = {"Gryffindor": 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin": 0}

yourHouse = None

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Sorting Hat")
window.iconbitmap("hat.ico")

#
style = ttk.Style()
window.tk.call("source", "Azure/azure.tcl")
window.tk.call("set_theme", "dark")
# Frames
topFrame = ttk.Frame(window)
bottomFrame = ttk.Frame(window)
leftFrame = ttk.Frame(bottomFrame)
rightFrame = ttk.Frame(bottomFrame)
endFrame = ttk.Frame(window)

# Widgets
label1 = ttk.Label(topFrame, text="im the hat", font="Calibri 15 bold")
label2 = ttk.Label(
    endFrame, text=f"Your house is...{yourHouse}", font="Calibri 35 bold"
)

button1 = ttk.Button(
    leftFrame, text="button1", command=lambda: updateScore(question, 0)
)
button2 = ttk.Button(
    leftFrame, text="button2", command=lambda: updateScore(question, 1)
)
button3 = ttk.Button(
    rightFrame, text="button3", command=lambda: updateScore(question, 2)
)
button4 = ttk.Button(
    rightFrame, text="button4", command=lambda: updateScore(question, 3)
)

# pack
topFrame.pack(fill="both", expand=True)
bottomFrame.pack(fill="both", expand=True)
leftFrame.pack(side="left", fill="both", expand=True)
leftFrame.pack_propagate(False)
rightFrame.pack(side="right", fill="both", expand=True)
rightFrame.pack_propagate(False)

label1.pack(fill="both", expand=True)

button1.pack(fill="both", expand=True, padx=4, pady=4)
button1.pack_propagate(False)
button2.pack(fill="both", expand=True, padx=4, pady=4)
button2.pack_propagate(False)
button3.pack(fill="both", expand=True, padx=4, pady=4)
button3.pack_propagate(False)
button4.pack(fill="both", expand=True, padx=4, pady=4)
button4.pack_propagate(False)

# main
question = 0


def updateScore(questionNumber, answer):

    global question

    houses[answerWeight[questionNumber][answer][0]] += answerWeight[questionNumber][
        answer
    ][1]
    houses[answerWeight[questionNumber][answer][2]] += answerWeight[questionNumber][
        answer
    ][3]
    if question < 7:
        question += 1
        askQuestion(question)
    else:
        endScreen()


def askQuestion(questionNumber):
    label1.config(text=questionBank[questionNumber])
    button1.config(text=answerBank[questionNumber][0])
    button2.config(text=answerBank[questionNumber][1])
    button3.config(text=answerBank[questionNumber][2])
    button4.config(text=answerBank[questionNumber][3])


def endScreen():
    findHouse()
    topFrame.pack_forget()
    bottomFrame.pack_forget()
    label2.pack(fill="both", expand=True)
    endFrame.pack(fill="both", expand=True)


def findHouse():
    global yourHouse
    yourHouse = max(houses, key=houses.get)
    label2.config(text=f"You belong to {yourHouse}")


askQuestion(question)

# run
window.mainloop()
