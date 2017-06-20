from tkinter import *

calculator = Tk()
calculator.title("CALCULATOR")
calculator.resizable(0, 0)

class Application(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.createWidgets()

	def createWidgets(self):
		self.display = Entry(self, font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
		self.display.insert(0, "0")
		self.display.grid(row=0, column=0, columnspan=5)

#This is the First Row
		self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=1)
		self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=1)
		self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=1)
		self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

		self.timesButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=1)
		self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=1)
		self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")

#This is the Second Row
		self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=1)
		self.fourButton.grid(row=2, column=0, sticky="NWNESWSE")

		self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=1)
		self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE")

		self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=1)
		self.sixButton.grid(row=2, column=2, sticky="NWNESWSE")

		self.divideButton = Button(self, font=("Helvetica", 11), text="/", borderwidth=1)
		self.divideButton.grid(row=2, column=3, sticky="NWNESWSE")

		self.percentageButton = Button(self, font=("Helvetica", 11), text="%", borderwidth=1)
		self.percentageButton.grid(row=2, column=4, sticky="NWNESWSE")

#This is the Third Row
		self.Button = Button(self, font=("Helvetica", 11), text="7", borderwidth=1)
		self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=1)
		self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=1)
		self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

		self.timesButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=1)
		self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=1)
		self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")

#This is the Fourth Row
		self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=1)
		self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=1)
		self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=1)
		self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

		self.timesButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=1)
		self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=1)
		self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")


app = Application(calculator).grid()		
calculator.mainloop()
