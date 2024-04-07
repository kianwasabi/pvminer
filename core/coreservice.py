class CoreService:
    def __init__(self):
        self.own_hashrate = 0
        self.invest = 0
        self.timealive = 0
        self.power_per_miner = 0
        self.number_miner = 0
    def grenzkosten(self):
        grenzkosten = (gesamtertrag_btc*(eigene_hashrate)/gesamthashrate*btc_preis-(gewinnfaktor*invest)/lebensdauer)/(anzahl_miner*leistung_pro_miner)
        return grenzkosten