def start():
	root = Tk()
	canvas = Canvas(root, width=1800, height = 1050)
	Button = Button(root, text= "Click to Start")
	Button.pack()
	Button.place(x=598, y=824)
	button.
	root.mainloop()

def invadv():
	canvas = Canvas(root, width=1800, height = 1050)
	root = Tk()
	frame = Frame(root)
	Button = Button(root, text= "Investment Advice")
	root.mainloop()

def moneyinvest(): 
	canvas = Canvas(root, width=1800, height = 1050)
	root = Tk()
	frame = Frame(root)
	Button = Button(root, text= "How much money do you want to invest?")
	root.mainloop()

def lt(): #TODO: Use functions for machine learning but long term here
	root = Tk()
	canvas = Canvas(root, width=1800, height = 1050)
	frame = Frame(root)
	text1 = Text(top)
	text1.insert(INSERT, "You have selected a Long-Term Investment")
	text1.insert(END, ".")
	text1.pack()
	root.mainloop()

def st(): #TODO: Use functions for machine learning but short term here
	root = Tk()
	canvas = Canvas(root, width=1800, height = 1050)
	frame = Frame(root)
	text2 = Text(top)
	text2.insert(INSERT, "You Have Selected a Short-Term Investment")
	text2.insert(END, ".")
	text2.pack()
	root.mainloop()

def stlt():
	root = Tk()
	canvas = Canvas(root, width=1800, height = 1050)
	frame = Frame(root)
	LongTerm = Button(root, text="Long-Term")
	ShortTerm = Button(root, text="Short-Term")
	LongTerm.pack()
	ShortTerm.pack()
	LongTerm.config(command=lt)
	ShortTerm.config(command=st)
	root.mainloop()

def v():
	frame = Frame(root)
	root = Tk()
	canvas = Canvas(root, width=1800, height = 1050)
	hv = Button(root)
	hv.pack()
	hv.config(command) #Add Volatility Graph/Suggestions (ML)
	lv = Button(root)
	lv.pack()
	root.mainloop()


from Tkinter import *
from PIL import ImageTk, Image

start()


