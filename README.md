A Whirlwind Introduction to Python Scripting
==============================================

This repository is a stand-alone workshop developed by the KU chapter of the ACM, designed to introduce
novice programmers to Python scripting.  The beginning consists of a brief overview of syntax, which segues
into an overview of a boilerplate application.  Participants fill in their parts of the skeleton application to
create a simple GUI that displays weather data and radar for their area.

The workshop was designed to span about an hour, so much of the application code is already present.
This application was modified from a more extensive previous version to fit the shorter time format
See the slideshow for a guided overview of the material, and the "complete_example" directory for its namesake.

This workshop is suitable for freshman CS students with high school programming experience, or non-majors with
an interest in basic Python file and data manipulation.

#Dependencies#
The example project requires a few libraries which you may not have installed on your machine.  They are generally helpful to have, but you can modify the project to do without a few of them.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```bash
sudo apt-get install python-bs4
```


[ImageMagick](http://www.imagemagick.org/script/index.php)
```bash
sudo apt-get install imagemagick
```

[TKinter](https://wiki.python.org/moin/TkInter)
```bash
sudo apt-get install python-tk
```


#Alternative setup#
If your university is like mine, you may not be able to directly install the above.  An alternate way to get set up is to use a virtual environment.  The *virtualenv* package lets you create your own little python installation and environment path in which you can install whatever you want using the "pip" Python installer.  After creating the virtual environment with the commands below, you can start using it with the activate command, which will be a script that lives in the folber you created for your virtual environment.

Install virtualenv (If you can't do this, the rest won't work)
```bash
sudo apt-get install python-virtualenv
```

Create a virtual environment in the folder "myVirtualEnv"
```bash
virtualenv myVirtualEnv
```

Start using the virtual environment, you will see the name of your environment added in front of your command prompt.
```bash
source myVirtualEnv/bin/activate
```

Stop using the virtual environment, and return to normal
```bash
deactivate
```

If you finished the above successfully, enter the commands below (while in your virtual environment) to install the dependencies.  The Tkinter package is included in the virtual environment installation above.
```bash
pip install beautifulsoup4
```

###### Note to the style police - The project files use block comments for informational sections, and line comments for others.  This approach makes it easier for participants to quickly identify where they need to modify code, since our text editors highlight line comments in bright colors.  Please refrain from death threats and name-calling.
