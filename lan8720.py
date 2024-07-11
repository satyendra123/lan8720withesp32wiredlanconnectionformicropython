import network

class Lan8720:
    def __init__(self):
        self.i = network.LAN(mdc=23, mdio=18, power=None, phy_addr=0)
    
    def active(self):
        self.i.active(True)
        self.i.ifconfig('dhcp')

    def ifconfig(self):
        return self.i.ifconfig()