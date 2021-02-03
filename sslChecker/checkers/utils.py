import requests
import OpenSSL
import ssl
import socket


def checkHTTPOK(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


def checkVALIDITY(url):
    response = requests.get(url)
    if response.is_permanent_redirect:
        return False
    else:
        return True


def checkSSLNOTEXPIRED(url):
    try:
        cert = ssl.get_server_certificate((url, 443))
    except:
        return False
    certificate = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM, cert)
    return not certificate.has_expired()


class CheckRunner():
    checks = []
    url = ''

    def __init__(self, checks, url):
        self.checks = checks
        self.url = url
        vars(self)['VALIDITY'] = checkVALIDITY
        vars(self)['HTTPOK'] = checkHTTPOK
        vars(self)['SSLNOTEXPIRED'] = checkSSLNOTEXPIRED

    def execute(self):
        isSuccess = True
        for ch in self.checks:
            isIndependantSuccess = vars(self)[ch.check](self.url)
            if not isIndependantSuccess:
                isSuccess = False
        return isSuccess
