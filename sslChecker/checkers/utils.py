import requests


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

# TODO add ssl certificate verif
# pool = req.connection.poolmanager.connection_from_url('https://httpbin.org')
# conn = pool.pool.get()
# # get() removes it from the pool, so put it back in
# pool.pool.put(conn)
# print(conn.sock.getpeercert())


class CheckRunner():
    checks = []
    url = ''

    def __init__(self, checks, url):
        self.checks = checks
        self.url = url
        vars(self)['VALIDITY'] = checkVALIDITY
        vars(self)['HTTPOK'] = checkHTTPOK

    def execute(self):
        isSuccess = True
        for ch in self.checks:
            isIndependantSuccess = vars(self)[ch.check](self.url)
            if not isIndependantSuccess:
                isSuccess = False
        return isSuccess
