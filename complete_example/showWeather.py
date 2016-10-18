import Tkinter as tk    #The GUI module
import os               #Allows system commands to be called
import datetime		#Access to system time

class Display(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit',command=self.quit)
		self.quitButton.grid(padx=5, pady=5, row=16, column=2)
		self.pic = tk.PhotoImage(file="radar.gif")
		self.can = tk.Canvas(self, width=326, height=326)

		'''
		The anchor option below refers to how the image will be
		positioned within the canvas.  Here, we have entered the 
		coordinates of the exact center of the canvas. Anchor will 
		center the image at these coordinates.
		'''
		self.can.create_image(163,163, anchor=tk.CENTER, image=self.pic)

		'''
		The grid manager determines the position and any padding
		sticky option refers to what edge it will align with
		from N,S,E,W.  Stretching is done by specifying two
		attributes concatenated, eg E+W means stretch horizontally
		rowspan means this object will overwrite 10 rows. This 
		will stop the grid manager from expanding the entire row
		to the size of the image
		'''
		self.can.grid(row=0, column=0, padx=5, sticky=tk.N, rowspan=6)

		self.buildTable()

	def buildTable(self):

		#make a new frame nested within our main one
		self.table = tk.Frame(self)

		#open our input file, whih was filled by weatherGet script
		input = open("tableDump.txt", "r")
		valuesList = []

		#while there are lines left to read, load them into a list
		for lastLine in input.readlines():
			valuesList.append(lastLine)
		input.close()

		#The first line of our file comes in handy here
		size = int(valuesList[0])

		#Replace it by the current time now that we don't need it anymore
		valuesList[0] = str(datetime.datetime.now())

		'''
		Create text labels within our table frame and grid them
		note that by specifiying self.table, the grid manager
		knows to arrange the labels within this inner frame


		Here, I've added a word wrap for entries longer than 40 characters
		This is a workaround to the behavior of the grid tool; it will stretch
		the column to fit the text, which ditorts the whole GUI.  Instead,
		if it finds a long entry, it sets the wrap flag to true and splits
		the excess into the 'otherpart' string, and creates a separate label
		for the excess text
		'''
		for i in range (0, size):
			myText = valuesList[i]
			otherPart = ""
			wrap = False

			if len(myText) > 40:
				otherPart = myText[39:]
				myText = myText[:39]
				wrap = True

			'''
			The frame widget allows for borders to be specified.  By placing
			each label in a frame with a thin border, the effect is a
			table when they are all placed next to each other.
			'''
			temp = tk.Frame(self.table, borderwidth=1, relief=tk.SOLID)
			temp2 = tk.Label(temp, text=myText).grid(sticky=tk.W + tk.E)
			temp.grid(sticky=tk.W+tk.E)

			if wrap:
				temp = tk.Frame(self.table, borderwidth=1, relief=tk.SOLID)
				temp2 = tk.Label(temp, text=otherPart).grid(sticky=tk.W + tk.E)
				temp.grid(sticky=tk.W+tk.E)

		#grid our table frame into the main one
		self.table.grid(row=0, column=2, padx=25, pady=25, sticky=tk.E + tk.W, rowspan=15)

myDir = "./"

print "\nFetching weather data . . .\n"
output = "python " + myDir + "getWeather.py"
sysReturn = os.system(output)


#The final step is instantiating our display and showing it.
#Assemble display
app=Display()
#Set label
app.master.title('Weather Console')
#Display as a windowed app
app.mainloop()
