import sys
import webbrowser
import wikipedia
import requests
import os


def isNetworkConnected():
    try:
        i = wikipedia.summary("linux")
        if i == "":
            pass
        return True
    except ConnectionError or ConnectionRefusedError or requests.ConnectionError:
        return False


def openChrome(link=''):
    try:
        os.system(f"google-chrome {link}")
    except OSError or FileNotFoundError:
        print("\033[91m[ERROR]: Google Chrome is not installed.")


def openFirefox(link=''):
    try:
        os.system(f"firefox {link}")
    except OSError or FileNotFoundError:
        print("\033[91m[ERROR]: Firefox is not installed.")


def openGoogle(defaultBrowser='google-chrome'):
    try:
        os.system(f"{defaultBrowser} www.google.com")
    except OSError or FileNotFoundError:
        try:
            os.system(f"firefox www.google.com")
        except OSError or FileNotFoundError:
            print("\033[91m[ERROR]: Unable to find a WebBrowser")


def openYoutube(defaultBrowser='google-chrome'):
    try:
        os.system(f"{defaultBrowser} www.youtube.com")
    except OSError or FileNotFoundError:
        try:
            os.system(f"firefox www.youtube.com")
        except OSError or FileNotFoundError:
            print("\033[91m[ERROR]: Unable to find a WebBrowser")


def openYahoo(defaultBrowser='google-chrome'):
    try:
        os.system(f"{defaultBrowser} www.yahoo.com")
    except OSError or FileNotFoundError:
        try:
            os.system(f"firefox www.yahoo.com")
        except OSError or FileNotFoundError:
            print("\033[91m[ERROR]: Unable to find a WebBrowser")


def playYoutubeVideo(topic: str) -> str:
    """Play a YouTube Video"""
    if isNetworkConnected():
        pass
    else:
        print("Connect to a network")
        sys.exit(0)
    # _checkNetwork(__exitMsg__='\033[91m[ERROR]:\033[93m Network required to use this function. Connect to network')
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

    webbrowser.open(f"https://www.youtube.com{lst[count - 5]}")

    return f"https://www.youtube.com{lst[count - 5]}"


def openGmail():
    if isNetworkConnected():
        pass
    else:
        print("Connect to a network")
        sys.exit(0)
    webbrowser.open(f'https://mail.google.com/mail/')


def searchWeb(topic: str) -> None:
    if isNetworkConnected():
        pass
    else:
        print("Connect to a network")
        sys.exit(0)
    """Searches About the Topic on Google"""

    link = f"https://www.google.com/search?q={topic}"
    webbrowser.open(link)


def openURL(siteURL: str) -> None:
    if isNetworkConnected():
        pass
    else:
        print("Connect to a network")
        sys.exit(0)
    webbrowser.open(siteURL)


def searchWikipedia(topic: str, lines: int = 3, return_value: bool = False):
    """Gives Information on the Topic"""
    if isNetworkConnected():
        pass
    else:
        print("Connect to a network")
        sys.exit(0)
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
    try:
        url = f"https://render-tron.appspot.com/screenshot/{link}/?width={width}&height={height}"
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(os.path.join(path, filename), "wb") as file:
                for chunk in response:
                    file.write(chunk)
    except ConnectionError or requests.ConnectionError or Exception as e:
        if e != "":
            print("Connect to a network!.")
        else:
            print(e)