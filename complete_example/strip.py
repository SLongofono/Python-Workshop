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
'''

def weatherParse(s):
	myList = []

	#Abbreviations to help keep track of what we're looking at
	hum = s.find("Humidity")
	dew = s.find("Dew Point")
	win = s.find("Wind")
	winG = s.find("Wind Gust")
	pres = s.find("Pressure")
	con = s.find("Conditions")
	vis = s.find("Visibility")
	uv = s.find("UV")
	clo = s.find("Clouds")
	max = s.find("Yesterday's Maximum")
	min = s.find("Yesterday's Minimum")
	sun = s.find("Sunrise")
	set = s.find("Sunset")
	end = s.find("Moon")
	result = ""

	myList = []

    	#The find method returns -1 if it can't find the argument.  Wind gust is not
    	#always present, so we need to check if it is, and act accordingly
	if(winG == -1):

	    '''
	    Each of our abbreviated names represents the index where that label
	    begins.  Instead of trying to work out some way to separate the labels
	    from the values, we simply split our string at the index of the next
	    label.  This works so long as we know how many labels to expect and
	    the order they are in.
   	    '''
		myList.append(s[0:hum])
		myList.append(s[hum:dew])
		myList.append(s[dew:win])
		myList.append(s[win:pres])
		myList.append(s[pres:con])
		myList.append(s[con:vis])
		myList.append(s[vis:uv])
		myList.append(s[uv:clo])
		myList.append(s[clo:max])
		myList.append(s[max:min])
		myList.append(s[min:sun])
		myList.append(s[sun:set])
		myList.append(s[set:end])
	else:
		myList.append(s[0:hum])
		myList.append(s[hum:dew])
		myList.append(s[dew:win])
		myList.append(s[win:winG])
		myList.append(s[winG:pres])
		myList.append(s[pres:con])
		myList.append(s[con:vis])
		myList.append(s[vis:uv])
		myList.append(s[uv:clo])
		myList.append(s[clo:max])
		myList.append(s[max:min])
		myList.append(s[min:sun])
		myList.append(s[sun:set])
		myList.append(s[set:end])

	return myList

#Open the output file of our web scraper
x = open("testDump.txt", "r")
rawString = x.read()
x.close

#remove html tags
rawString = reNoTags(rawString)

#remove excess spaces
rawString = stripWhiteSpace(rawString)

#find our table values by using a unique nearby word
start = rawString.find("Observed")
end = rawString.find("Moon")
rawString = rawString[start:end]

#now trim off the excess since we have isolated what we want
start = rawString.find("Temperature")
rawString = rawString[start:]

#split it into a list, with a label and the corresponding value for each element
myList = weatherParse(rawString)


#Open a text file and write the number of entries as the first line
x = open('tableDump.txt', 'w')
x.write(str(len(myList)) + '\n')
for item in myList:
	x.write(item)
	x.write('\n')
x.close()
