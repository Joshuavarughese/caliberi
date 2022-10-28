import sys
import threading
import webbrowser as webBrowser
from typing import Optional
from email.message import EmailMessage
from email.mime.text import MIMEText
from typing import Union
import time
import os
import re
import datetime
import smtplib
import platform
import requests
import wikipedia
from PIL.Image import open as __openBox

osname = platform.system()

"""
try:
    i = wikipedia.summary("windows")
except Exception as e:
    print(
         "Network connection required! Failed to connect. Some function cannot be used.\033[39m")
    pass

"""


# interUse Libraries


def _checkNetwork(__exitMsg__):
    try:
        requests.get('https://www.google.com')
        return True
    except ConnectionError or requests.RequestException or requests.ConnectionError or requests.ConnectTimeout:
        print(__exitMsg__)
        sys.exit(0)


# Caliberi Libraries


class attributes:
    os = platform.system()
    distribution = platform.linux_distribution()[0]
    ditro = platform.linux_distribution()[0]
    version = platform.linux_distribution()[1]
    ver = platform.linux_distribution()[1]
    processor = platform.processor()
    architecture = platform.architecture()
    machine = platform.machine()
    kernel = platform.release()
    system = platform.system()
    deviceName = platform.node()
    pythonVersion = platform.python_version()
    pythonCompiler = platform.python_compiler()


def getCurrentTime(format="%H:%M:%S"):
    """
    %H Hour
    %M Minutes
    %S Seconds
    you can decide the separator symbols (:, /, |)
    :param format:
    :return:
    """
    return datetime.datetime.now().time().strftime(format)


def getCurrentDate(format: str = "%D/%M/%Y"):
    """
    _format type:\n
        %Y Year\n
        %M Month\n
        %D Day\n
    example: d1 = getCurrentDate('%D/%M/%Y') #oder is date/month/year\n
    :param format :
    :return:
    """
    _year = str(datetime.datetime.today().year)
    _month = str(datetime.datetime.today().month)
    _day = str(datetime.datetime.today().day)
    _date = format
    if '%Y' in format:
        _date = _date.replace('%Y', _year)
    elif '%y' in format:
        _date = _date.replace('%y', _year)

    if '%M' in format:
        _date = _date.replace('%M', _month)
    elif '%m' in format:
        _date = _date.replace('%m', _month)

    if '%D' in format:
        _date = _date.replace('%D', _day)
    elif '%d' in format:
        _date = _date.replace('%d', _day)

    return _date


def getSysInfo(attributes):
    return attributes


def showImage(file: str):
    try:
        # subprocess.getoutput(f'eog {os.path.join(file)}')
        os.system(f"eog {os.path.join(file)}")
    except FileNotFoundError or FileExistsError:
        print(f'\033[91m[Error]: Image not found!. File \033[43m{file}\033[49m does not exists.')


def takeScreenshot(file_name: str = "screenshot.png",
                   delay: int = 2,
                   show: bool = True):
    """
    Take Screenshot of the Current screen\n
    >>file_name = The name with path of destination
        eg: takeScreenshot(file_name='/home/user/Desktop/filename.png')
        if you give simply name in the variable then the file will be\n
        stored at the current working dir\n
            eg: takeScreenshot(file_name='name.png')
            you can see a name.png file on the location where the program file exists\n

    >>delay = The time seconds to wait
        it will wait of the seconds given and then take the screenshot\n
        its default value is 2\n
        \n
    >>show = Bool variable
        \tOn True it will display the taken screenshot\n
        \tOn False it will do nothing\n
    """
    time.sleep(delay)
    os.system(f'gnome-screenshot -f \'{os.path.join(file_name)}\'')
    if show:
        os.system(f'eog {os.path.join(file_name)}')


def copyFile(file: str, destination: str):
    """
    This function helps to copy a file to another destination\n
    >>file = The file which is need to be copied\n
    >>destination = The location where the file need to be copied\n

    It will copy the file to the destination\n
    If the file is in the location where the program file exists then you can just type the name of the file\n
    If not then you need to give the full path to the file in variable file
    """
    os.system(f'cp {file} {destination}')


def makeDir(path: str):
    """
    This function will make a Directory in the path given
    eg: makeDir('/home/user/Desktop/dirname')
    In this case it will make a directory in the path given. Here in this, you can see a new directory dirname in Desktop folder.
    """
    os.system(f'mkdir {os.path.join(path)}')


def removeDir(path: str):
    os.system(f'rmdir {os.path.join(path)}')


def makeFile(name: str, openTextEditor: bool = False):
    if openTextEditor:
        os.system(f'gedit {os.path.join(name)}')
    else:
        os.system(f'touch {os.path.join(name)}')


def deleteFile(file: str):
    try:
        os.system(f'rm {os.path.join(file)}')
    except FileNotFoundError or FileExistsError:
        print(f"\033[91m[ERROR]: Requested file {file} not found!")
        sys.exit(0)


def moveDir(file: str, destination: str):
    try:
        os.system(f'cp -r {file} {destination}')
        if True:
            os.system(f"rm /{file}/*")
    except FileNotFoundError or FileExistsError:
        print(f"\033[91m[ERROR]: Requested file {file} not found!")
        sys.exit(0)


def copyDir(dirName: str, destination: str):
    try:
        os.system(f'cp {dirName} {destination}')
    except FileNotFoundError or FileExistsError:
        print(f"\033[91m[ERROR]: Requested file {dirName} not found!")
        sys.exit(0)


def getSystemName():
    _system = os.name.lower()
    if "posix" in _system:
        _system = f"Linux {platform.linux_distribution()[0]} {platform.linux_distribution()[1]}"
    return _system


class UnableToAccessApi(Exception):
    """unable to access api"""
    pass


def playYoutubeVideo(topic: str) -> str:
    """Play a YouTube Video"""
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    url = f"https://www.youtube.com/results?q={topic}"
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/results":
        raise Exception("No Video Found for this Topic!")

    webBrowser.open(f"https://www.youtube.com{lst[count - 5]}")

    return f"https://www.youtube.com{lst[count - 5]}"


def openGoogle():
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    webBrowser.open(f'https://www.google.com')


def openYoutube():
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    webBrowser.open(f'https://www.youtube.com')


def openGmail():
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    webBrowser.open(f'https://mail.google.com/mail/')


def convertImgToAscii(
        img_path: str,
        output_file: Optional[str] = "AsciiFile"
) -> str:
    """Convert an Image to ASCII Art"""

    img = __openBox(os.path.join(img_path)).convert("L")

    width, height = img.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    pixels = img.getdata()

    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [
        new_pixels[index: index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]
    ascii_image = "\n".join(ascii_image)

    with open(f"{output_file}.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image


# ------------------------------------------------- #


def searchWeb(topic: str) -> None:
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    """Searches About the Topic on Google"""

    link = f"https://www.google.com/search?q={topic}"
    webBrowser.open(link)


def openURL(siteURL: str) -> None:
    webBrowser.open(siteURL)


def searchWikipedia(topic: str, lines: int = 3, return_value: bool = False) -> Optional[str]:
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    """Gives Information on the Topic"""

    data = wikipedia.summary(topic, sentences=lines)
    print(data)
    if return_value:
        return data


def webScreenshot(link: str,
                  filename: str = "Screenshot.jpg",
                  path: str = os.getcwd(),
                  width: int = 1920,
                  height: int = 1080,
                  ) -> None:
    """Take Screenshot of Any Website Without Opening it"""

    url = f"https://render-tron.appspot.com/screenshot/{link}/?width={width}&height={height}"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(path, filename), "wb") as file:
            for chunk in response:
                file.write(chunk)


def shutdownSystem(time: int = 20) -> None:
    """Schedules a Shutdown after the Specified Time"""
    """
    if "window" in osname.lower():
        cont = f"shutdown -s -t {time}"
        error_code = os.system(cont)
        if error_code in [winerror.ERROR_SHUTDOWN_IN_PROGRESS, 1115]:
            print("A Shutdown Process has already been Scheduled!")
        else:
            print(f"Your System will Shutdown in {time} Seconds!")
    """
    if "linux" in osname.lower():
        cont = f"shutdown -h {time}"
        os.system(cont)
        print(f"Your System will Shutdown in {time} Minutes!")

    elif "darwin" in osname.lower():
        cont = f"shutdown -h -t {time}"
        os.system(cont)
        print(f"Your System will Shutdown in {time} Minutes!")

    else:
        raise Warning(
            f"Available on Linux only, can't Execute on {osname}"
        )


def cancelShutdown() -> None:
    """Cancels the Scheduled Shutdown"""
    """
    if "window" in osname.lower():
        error_code = os.system("shutdown /a")
        if error_code == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
            print(
                "Shutdown Cancellation process has been Aborted! [NO Shutdown Scheduled]"
            )
        else:
            print("Shutdown has been Cancelled!")"""

    if "linux" in osname.lower():
        os.system("shutdown -c")
        print("Shutdown has been Cancelled!")

    elif "darwin" in osname.lower():
        os.system("killall shutdown")
        print("Shutdown has been Cancelled!")

    else:
        raise Warning(
            f"Available on Windows, Mac and Linux only, can't Execute on {osname}"
        )


class UnsupportedEmailProvider(Exception):
    pass


def sendMail(email_sender: str,
             password: str,
             subject: str,
             message: Union[str, MIMEText],
             email_receiver: str,
             ) -> None:
    """Send an Email"""
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
    domain = re.search("(?<=@)[^.]+(?=\\.)", email_sender)

    hostnames = {
        "gmail": "smtp.gmail.com",
        "yahoo": "smtp.mail.yahoo.com",
        "outlook": "smtp.live.com",
        "aol": "smtp.aol.com",
    }

    hostname = None
    for x in hostnames:
        if x == domain.group():
            hostname = hostnames[x]
            break

    if hostname is None:
        raise UnsupportedEmailProvider(f"{domain.group()} is not Supported Currently!")

    with smtplib.SMTP_SSL(hostname, 465) as smtp:
        smtp.login(email_sender, password)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content(message)

        smtp.send_message(msg)
        print("Email Sent Successfully!")


def sendHmail(email_sender: str, password: str, subject: str, html_code: str, email_receiver: str
              ) -> None:
    """Send an Email with HTML Code"""
    _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')

    message = MIMEText(html_code, "html")
    sendMail(email_sender, password, subject, message, email_receiver)


# Color func

CSI = '\033['
OSC = '\033]'
BEL = '\007'


def _code_to_chars(code):
    return CSI + str(code) + 'm'


def set_title(title):
    return OSC + '2;' + title + BEL


def clear_screen(mode=2):
    return CSI + str(mode) + 'J'


def clear_line(mode=2):
    return CSI + str(mode) + 'K'


class _AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation, we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, _code_to_chars(value))


class _AnsiCursor(object):
    def __init__(self):
        super(_AnsiCursor, self).__init__()
        self.f = 0

    @staticmethod
    def UP(n=1):
        return CSI + str(n) + 'A'

    @staticmethod
    def DOWN(n=1):
        return CSI + str(n) + 'B'

    @staticmethod
    def FORWARD(n=1):
        return CSI + str(n) + 'C'

    @staticmethod
    def BACK(n=1):
        return CSI + str(n) + 'D'

    @staticmethod
    def POS(x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'


class Fore(_AnsiCodes):
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    RESET = '39'

    # These are fairly well-supported, but not part of the standard.
    LIGHTBLACK_EX = '90'
    LIGHTRED_EX = '91'
    LIGHTGREEN_EX = '92'
    LIGHTYELLOW_EX = '93'
    LIGHTBLUE_EX = '94'
    LIGHTMAGENTA_EX = '95'
    LIGHTCYAN_EX = '96'
    LIGHTWHITE_EX = '97'


class Back(_AnsiCodes):
    BLACK = "40"
    RED = "41"
    GREEN = "42"
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'
    RESET = '49'

    # These are fairly well-supported, but not part of the standard.
    LIGHTBLACK_EX = '100'
    LIGHTRED_EX = '101'
    LIGHTGREEN_EX = '102'
    LIGHTYELLOW_EX = '103'
    LIGHTBLUE_EX = '104'
    LIGHTMAGENTA_EX = '105'
    LIGHTCYAN_EX = '106'
    LIGHTWHITE_EX = '107'


class Style(_AnsiCodes):
    BRIGHT = 1
    DIM = 2
    NORMAL = 22
    RESET_ALL = 0
    BOLD = 1
    UNDERLINE = 4


TextColor = Fore()
TextBackgroundColor = Back()
TextStyle = Style()


class console:
    @staticmethod
    def putText(text: str, options=None, end='\n'):
        if options == '' or options is None:
            print(f'{text}', end=end)
        else:
            __index__ = int(len(options))
            print(
                f'{options[0 > __index__]}{options[1 < __index__]}{options[2 < __index__]}{options[3 < __index__]}{options[4 < __index__]}{options[5 < __index__]}{options[6 < __index__]}{text}\033[49m\033[39m',
                end=end)

    @staticmethod
    def setUnderlinedText():
        print('\033[4m', end='')

    @staticmethod
    def RESET():
        print('\033[0m\033[49m\033[39m', end='')

    class setTextColor:
        @staticmethod
        def BLACK():
            print('\033[90m', end='')
            return '\033[90m'

        @staticmethod
        def RED():
            print('\033[91m', end='')
            return '\033[91m'

        @staticmethod
        def GREEN():
            print('\033[92m', end='')
            return '\033[92m'

        @staticmethod
        def YELLOW():
            print('\033[93m', end='')
            return '\033[93m'

        @staticmethod
        def BLUE():
            print('\033[94m', end='')
            return '\033[94m'

        @staticmethod
        def MAGENTA():
            print('\033[95m', end='')
            return '\033[95m'

        @staticmethod
        def CYAN():
            print('\033[96m', end='')
            return '\033[96m'

        @staticmethod
        def WHITE():
            print('\033[97m', end='')
            return '\033[97m'

        @staticmethod
        def DEFAULT():
            print('\033[39m', end='')
            return '\033[39m'

    class setTextBackground:
        @staticmethod
        def BLACK():
            print('\033[100m', end='')
            return '\033[100m'

        @staticmethod
        def RED():
            print('\033[101m', end='')
            return '\033[101m'

        @staticmethod
        def GREEN():
            print('\033[102m', end='')
            return '\033[102m'

        @staticmethod
        def YELLOW():
            print('\033[103m', end='')
            return '\033[103m'

        @staticmethod
        def BLUE():
            print('\033[104m', end='')
            return '\033[104m'

        @staticmethod
        def MAGENTA():
            print('\033[105m', end='')
            return '\033[105m'

        @staticmethod
        def CYAN():
            print('\033[106m', end='')
            return '\033[106m'

        @staticmethod
        def WHITE():
            print('\033[107m', end='')
            return '\033[107m'

        @staticmethod
        def DEFAULT():
            print('\033[49m', end='')
            return '\033[49m'


class network:
    @staticmethod
    def isConnected():
        try:
            i = wikipedia.summary("windows")
            if i == "":
                pass
            return True
        except ConnectionError:
            return False


def stopAll():
    sys.exit(0)


class Thread:
    def __init__(self, target, args=()):
        self.target = target
        self.args = args
        self.__thread__ = threading.Thread(target=self.target, args=(self.args,))
        self._args = None

    def start(self):
        self.__thread__.start()

    def getActiveCount(self):
        self._args = self.args
        return threading.activeCount() - 1

    def activeCount(self):
        self._args = self.args
        return threading.activeCount() - 1


class File:
    """
    Create, Delete, Write, Read, WriteBytes, ReadBytes
    """
    def __init__(self, file, mode='w'):
        self.mode = mode
        self.file = os.path.join(file)

    def remove(self):
        os.system(f"rm {self.file}")

    def getText(self):
        file = open(self.file, 'r')
        if self.mode == 'rb':
            file = open(self.file, 'rb')
        elif self.mode == 't':
            file = open(self.file, 't')
        text = file.read()
        file.close()
        return text

    def write(self, text):
        file = open(self.file, 'w')
        if self.mode == 'a':
            file.close()
            file = open(self.file, 'a')
        file.write(text)
        file.close()

    def newLine(self, text):
        """
        Write the text in new line of the file
        :param text:
        :return: none
        """
        file = open(self.file, 'a')
        file.write(text)
        file.close()

    def append(self, text):
        file = open(self.file, 'a')
        file.write(text)
        file.close()

    def appendMode(self):
        self.mode = 'a'

    def changeMode(self, mode):
        self.mode = mode

    def makeExecutable(self, value='+x'):
        """
        value : executes chmod {value} {file}"""
        os.system(f"chmod {value} {self.file}")

    def execute(self, prefix='./'):
        """
        Execute the current file.
        prefix : it will be added to the first of the file. ./ is commonly used if it is makeExecutable(). to run a python file you may use prefix='python ' NOTE: a space is required after word if you give any other.
            eg: execute(prefix='python3 ')
        :param prefix:
        :return:
        """
        try:
            os.system(f"{prefix}{self.file}")
        except OSError or FileNotFoundError:
            print("\033[91m[ERROR]: Cannot execute the file!")
# !---------------------- END ----------------------! #