<h1>Caliberi Python Library (Linux)</h1>

<h4>Welcome to caliberi python library documentation</h4>
* Easy to use
* Makes your program easier
* Comparable with Systems

<h3>Lets start with import</h3>
Imports
    
    from caliberi import *

OR

    import Caliberi

<h4>Usages</h4>
Before that, lets look at the structure of library<br>
Caliberi(Lite) have three python files which can be imported<br>
They are:
* calib
* web
* calibmath
<br>calib is the main file. It has the basic functions and classes
<br>
___
<h3>calib</h3>
Functions:
* getCurrentTime()
* getCurrentDate()
* showImage()
* takeScreenshot()
* copyFile()
* makeDir()
* makeFile()
* deleteFile()
* moveDir()
* copyDir()
* getSystemName()
* playYoutubeVideo()
* openGoogle()
* openYoutube()
* openGmail()
* convertImgToAscii()
* searchWeb()
* openUrl()
* searchWikipedia()
* shutdownSystem()
* cancelShutdown()
* sendEmail()
* sendHmail()
<br>
Classes
  * console
  * network
  * Thread
  * File
  * Folder

<h3>getCurrentTime()</h3>
    --------------------------------
<br>
<h5>This function returns current time in a str variable.
Parameters format.</h5>

    getCurrentTime(format='%H %M %S')

<h5>In format %H indicate hours, %M for minutes & %S for seconds<br>
Any other string word putted on format will be returned as it is.<br>
for eg:</h5> <br>`time = getCurrentTime(format='%H:%M')`<br>
`print(time)`<br>
<h5>Here the output will be `hour:minute`, we use a separator : and it is returned as it. In this eg we donot get seconds as we have not given %S</h5><br>
----
<br>
<h3>getCurrentDate()</h3>
    --------------------------------<br>
This function will return current Date. Parameter format.<br>

    getCurrentDate(format='%D %M %Y')

In format %D indicate date, %M for month & %Y for year.<br>
Any other string word putted on format will be returned as it is.<br>
for eg:<br>`date = getCurrentDate(format='%D/%M/%Y')`<br>
`print(date)`<br>
Here the output will be `date/month/year`, we use a separator / and it is returned a it is.<br>
----
<h3>showImage()</h3>
    ------------------------<br>
This function will show image given to the parameter file.

    showImage(file='myimage.png')
In this eg it shows `myimage.png`.

---

<h3>takeScreenshot()</h3>
    ---------------------------------<br>
This function is used to take a Screenshot of the screen. Parameters file_name, delay, show.<br>

    takeScreenshot(file_name='myscreenshot.png', delay=2, show=True)
This function will take a screenshot after waiting {delay} seconds and saves  it as {file_name} & if show=True then it will show the taken image.
In the above eg it will take screenshot after `2` seconds and saves it as `myscreenshot.png` and shows the taken image.
<h2>Licensed Under MIT</h2>
<img src='OSIApproved_1.png'></img>

