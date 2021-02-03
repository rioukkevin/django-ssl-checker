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


class CheckRunner():
    VALIDITY = checkVALIDITY
    HTTPOK = checkHTTPOK

    checks = []
    url = ''

    def __init__(self, checks, url):
        self.checks = checks

    def execute(self):
        isSuccess = False
        for ch in self.checks:
            isIndependantSuccess = self[ch](self.url)
            if isIndependantSuccess:
                isSuccess = True
        return isSuccess
