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
    checks = []
    url = ''

    def __init__(self, checks, url):
        self.checks = checks
        self.url = url
        vars(self)['VALIDITY'] = checkVALIDITY
        vars(self)['HTTPOK'] = checkHTTPOK

    def execute(self):
        isSuccess = False
        for ch in self.checks:
            isIndependantSuccess = vars(self)[ch.check](self.url)
            if isIndependantSuccess:
                isSuccess = True
        return isSuccess
