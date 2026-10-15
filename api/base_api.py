import requests


class BaseApi:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    TIMEOUT = 10   # 全局超时 10 秒

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json",
        })

    def get(self, path, **kwargs):
        kwargs.setdefault("timeout", self.TIMEOUT)
        return self.session.get(f"{self.BASE_URL}{path}", **kwargs)

    def post(self, path, **kwargs):
        kwargs.setdefault("timeout", self.TIMEOUT)
        return self.session.post(f"{self.BASE_URL}{path}", **kwargs)

    def put(self, path, **kwargs):
        kwargs.setdefault("timeout", self.TIMEOUT)
        return self.session.put(f"{self.BASE_URL}{path}", **kwargs)

    def delete(self, path, **kwargs):
        kwargs.setdefault("timeout", self.TIMEOUT)
        return self.session.delete(f"{self.BASE_URL}{path}", **kwargs)