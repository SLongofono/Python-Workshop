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

		'''.
		The anchor option below refers to how the image will be
		positioned within the canvas.  Here, we have entered the 
		coordinates of the exact center of the canvas. Anchor will 
		center the image at these coordinates.
		'''
		self.can.create_image(163,163, anchor=tk.CENTER, image=self.pic)

		'''.
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

		'''.
		Create text labels within our table frame and grid them
		note that by specifiying self.table, the grid manager
		knows to arrange the labels within this inner frame
		'''

		# Enter your code here
		#
		# Step 1: For each item in our data list, create a frame
		# Step 2: For each frame, create a label
		# Step 3: For each frame, call grid
		#
		# Hint: Below is the code to add a single entry to our GUI data area
		# 	You will use the same exact format, except you need to repeat
		#	it for every item in our 'valuesList' variable
		#

		'''.
		The frame widget allows for borders to be specified.  By placing
		each label in a frame with a thin border, the effect is a
		table when they are all placed next to each other.
		'''
		temp = tk.Frame(self.table, borderwidth=1, relief=tk.SOLID)
		temp2 = tk.Label(temp, text=myText).grid(sticky=tk.W + tk.E)
		temp.grid(sticky=tk.W+tk.E)


		##### END OF YOUR CODE #####

		#grid our table frame into the main one
		self.table.grid(row=0, column=2, padx=25, pady=25, sticky=tk.E + tk.W, rowspan=15)


print "\nFetching weather data . . .\n"
# Your code here
# Step 1: make an OS command to run the getWeather.py script.



##### END OF YOUR CODE #####

'''.
The final step is instantiating our display and showing it.
This will assemble the display, add a title, and display it until
the quit button is clicked.
'''
app = Display()
app.master.title('Weather Console')
app.mainloop()
