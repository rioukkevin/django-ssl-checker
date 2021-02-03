import requests


def checkHTTPOK(url):
    response = requests.get(url)
    if response.ok:
        return True
    else:
        return False


def checkVALIDITY(url):
    response = requests.get(url)
    if response.is_permanent_redirect:
        return False
    else:
        return True
