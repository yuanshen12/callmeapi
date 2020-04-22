import requests
import json


class RunMain:
    # def __init__(self, url, method, data=None):
    #     self.res = self.run_main(url, method, data)

    def send_get(self, url, data=None):
        res = requests.get(url, data).json()
        return res

    def send_post(self, url, data=None):
        res = requests.post(url, data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    data = {
        "username": "liming",
        "password": "123456"
    }
    url = "http://127.0.0.1:8000/login/"
    run = RunMain()
    print(run.send_post(url, data))
