import urllib2
from urllib import urlretrieve
from bs4 import BeautifulSoup
import re
import os

'''
Change this to your zip code for now.  Later on, this can be populated with
command line arguments when it is called from the WConsole.py program
'''
zip = "66049"

'''
The mobile website is more simple and less likely to change.  Mobile phones
vary in software, platform, and ability, so the site itself is limited to
only basic html for compatibility.
'''
url = "http://m.wund.com/cgi-bin/findweather/getForecast?brand=mobile&query=" + zip

print "Connecting to wunderground . . .\n"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "lxml")

print "Writing raw data to testDump file . . .\n"

temp = open("testDump.txt", "w")
temp.write(soup.prettify().encode('UTF-8'))#best method name ever
temp.close()

print "Parsing weather data . . .\n"

'''
Below is a simple way to catch problems.  Typically, the OS will return
a zero if everything went well when a command was executed.  This
setup allows us to catch the number returned and see if anything went
wrong.
'''

sysReturn = os.system("python strip.py")
if sysReturn != 0:
	print "Oops, something went wrong, check the testDump.txt file for unusual data, and make sure strip.py is present.\n"

'''
Below is another way to catch problems.  Some things within the try: section
have the potential to crash the program.  The except: section will only
run if something goes wrong.  Here, we use some built-in features of exceptions
to print what went wrong.  When in doubt, put code in a try block, and follow
it with a catch block to recover if anything goes wrong.
'''
try:
	print "Retrieving radar image . . .\n"
	for link in soup.find_all('a'):  #grab all tags with the a keyword

	    #if any of these have a 'href' tag, check if it is the link to the radar
		if "feature=zoomradar" in str(link.get('href')):
			#print our the link
			imageUrl = "http://m.wund.com" + str(link.get('href'))
			print "Image found at: "
			print imageUrl

	page2 = urllib2.urlopen(imageUrl)
	soup2 = BeautifulSoup(page2, "lxml")

	#grab all 'img' tags
	for link in soup2.find_all('img'): 

	    # if the link source has "radblast"
		if "radblast" in str(link.get('src')):
			theImage = str(link.get('src'))

	# Enter your code here
	#
	# Step 1: Use the variable 'theImage' above to access the radar image on
	# 	  the weather underground website.  Save it locally.
	#
	# Step 2: Use the ImageMagick library to resize the image, and convert
	#	  it to a .gif file (if not already a .gif)
	#
	# Hint: look up Python urllib and find a way to retrieve media from an url.
	#	Alternately, you can look up the linux command 'wget'.
	#	Use the system.os() method to pass commands to the command line.
	#	They will be executed just as you type them (be careful!)


except Exception as err:
	print "Something blew up\n"
	print type(err)
	print err.args
	print err

