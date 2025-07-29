import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Authorization": "Bearer token123"}

    def get_data(self, endpoint):
        url = self.base_url + endpoint
        try:
            res = requests.get(url)
            return res.json()
        except Exception as e:
            print(e)

    def send_data(self, endpoint, payload):
        res = requests.post(self.base_url + endpoint, json=payload)
        return res.status_code == 200
