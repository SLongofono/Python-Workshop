import string
import re

'''
This method 'normalizes' whitespace in a string.  It removes tabs and newlines,
and replaces any blocks of spaces with a single space
'''
def stripWhiteSpace(s):
	return " ".join(s.rstrip().lstrip().split())

'''
This method removes html tags by systematically removing the indices between
angle brackets.  It assumes that the input is valid html, implying that
every open angle bracket has a matching close angle bracket.
'''
def reNoTags(s):
	return(re.sub('<[^<]+?>', '', s))

'''
This function is written to parse weather data from www.wunderground.com
Take a look at the output of the fetch script and figure out how to get the pieces
you want to show in your application.  This script is already set up to fetch and
save the data, and then call the weatherParse() method with the result.  You take
the argument 's' and grab the parts you want to display on the weather application.

Hint: All strings have a find() method, which will return the index of the argument
	passed in, or -1 if it does not exist.  For example:

	myString = "Hello world"
	worldStart = myString.find("world")
	print worldStart
	print myString[worldStart]

	This code would output '6', followed by 'w'.  Together with string slicing (Google it)
	you should be able to grab pieces of the weather information that you want
'''

def weatherParse(s):
	myList = []

	# Enter your code here
	# Step 1: grab the parts of the string s that you want to keep
	# Step 2: add them to myList

	return myList

'''Open the output file of our web scraper'''
x = open("testDump.txt", "r")
rawString = x.read()
x.close

'''remove html tags'''
rawString = reNoTags(rawString)

'''remove excess spaces'''
rawString = stripWhiteSpace(rawString)

'''find our table values by using a unique nearby word'''
start = rawString.find("Observed")
end = rawString.find("Moon")
rawString = rawString[start:end]

'''now trim off the excess since we have isolated what we want'''
start = rawString.find("Temperature")
rawString = rawString[start:]

'''split it into a list, with a label and the corresponding value for each element'''
myList = weatherParse(rawString)


'''Open a text file and write the number of entries as the first line'''

# Enter your code here
# Step 1: open an output file to write to
# Step 2: write the number of entries in myList to the first line
# Step 3: write each entry in myList to a line in the file
# Step 4: close the file, and check that the output is what you expected
