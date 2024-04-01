import requests 

class PowerGrid:
    def __init__(self):
        self.kilowatt = 0
    def get_kilowatt(self):
        response = requests.get("https://httpbin.org/get")
        payload = response.json()
        print(payload)
        self.kilowatt = payload['args']['kilowatt']
        return self.kilowatt

