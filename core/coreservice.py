class CoreService:
    def __init__(self):
        self.dummy = 0
    def grenzkosten(self):
        grenzkosten = (gesamtertrag_btc*(eigene_hashrate)/gesamthashrate*btc_preis-(gewinnfaktor*invest)/lebensdauer)/(anzahl_miner*leistung_pro_miner)
        return grenzkosten