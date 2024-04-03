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

class Mining:
    def __init__(self):
        self.price = 0
        self.hashrate = 0
        self.memepoolblocks = 0
    def get_mempoolblocks(self):
        response = requests.get("https://mempool.space/api/v1/fees/mempool-blocks")
        payload = response.json()
        print(payload)
        self.memepoolblocks = payload['args']['0']['totalFees']
        return self.memepoolblocks
    def get_price(self):
        response = requests.get("https://mempool.space/api/v1/prices")
        payload = response.json()
        print(payload)
        self.price = payload['args']['EUR']
        return self.price
    def get_hashrate(self):
        response = requests.get("https://mempool.space/api/v1/mining/hashrate/1d")
        payload = response.json()
        print(payload)
        self.hashrate = payload['args']['currentHashrate']
        return self.price