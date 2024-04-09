import requests 
import random

class PowerSource: 
    def __init__(self): 
        self.power = 0      #kW
    def get_power(self): 
        #response = requests.get("https://intradaytrading.org/get/price")
        #payload = response.json()
        #print(payload)
        self.power = random.randint(0,1000)
        return self.power
    
class IntradayTrading:
    def __init__(self):
        self.price_renewable_energy = 0      #EUR/MWh
    def get_price(self):
        #response = requests.get("https://intradaytrading.org/get/price")
        #payload = response.json()
        #print(payload)
        self.price_renewable_energy = random.randint(50,80)
        return self.price

class Mining:
    def __init__(self):
        self.price = 0          #EUR
        self.hashrate = 0       #TH
        self.memepoolblocks = 0 #Price of what? 
    def get_mempoolblocks(self):
        response = requests.get("https://mempool.space/api/v1/fees/mempool-blocks")
        payload = response.json()
        #print(payload)
        self.memepoolblocks = payload[0]['totalFees']
        return self.memepoolblocks
    def get_price(self):
        response = requests.get("https://mempool.space/api/v1/prices")
        payload = response.json()
        #print(payload)
        self.price = payload['EUR']
        return self.price
    def get_hashrate(self):
        response = requests.get("https://mempool.space/api/v1/mining/hashrate/1d")
        payload = response.json()
        #print(payload)
        self.hashrate = payload['currentHashrate']
        return self.hashrate