#this version works!
from Tkinter import *
import ttk
import random

def rollDice(*args):
	roll.set(random.randint(1,6))
	#diceImage = PhotoImage(file="one.png")
	diceImage = PhotoImage(file=(diceFaces[roll.get()-1]))
	rollDisplay = ttk.Label(mainframe,image=diceImage)
	rollDisplay.img = diceImage
	rollDisplay.grid(column=2,row=2,sticky=(W,E))

	
root = Tk()
root.title("Dice Roller")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

roll = IntVar()
diceFaces = ["one.gif","two.gif","three.gif","four.gif","five.gif","six.gif"]
#diceImage = PhotoImage()


rollButton = ttk.Button(mainframe,text="Roll the Dice", command=rollDice).grid(column=1,row=1,sticky=(W,E))
#rollDisplay = ttk.Label(mainframe,image=diceImage)
#rollDisplay.image = diceImage
#rollDisplay.grid(column=2,row=2,sticky=(W,E))
rollText = ttk.Label(mainframe,textvariable=roll).grid(column=2,row=3,sticky=(W,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>',rollDice)

root.mainloop()
