from gpiozero import DigitalOutputDevice

class Relais:
    def __init__(self, gpio_pin):
        self.bmc = gpio_pin
        self.channel = DigitalOutputDevice(gpio_pin)
    def turn_on(self):
        self.channel.on()
        print("Cluster on Channel "+str(self.bmc)+" turned on.")
    def turn_off(self):
        self.channel.off()
        print("Cluster on Channel "+str(self.bmc)+" turned off.")