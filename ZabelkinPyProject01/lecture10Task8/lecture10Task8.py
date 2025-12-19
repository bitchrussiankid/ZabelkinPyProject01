class Device:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def getInfo(self):
        return f"Device: {self.name}, power consumption: {self.power}W"


class SmartDevice(Device):
    def __init__(self, name, power, isConnected: bool):
        super().__init__(name, power)
        self.isConnected = isConnected

    def getInfo(self):
        return super().getInfo() + f", network connection: {self.isConnected}"


device = Device("Vacuum cleaner", 40)
print(device.getInfo())

smartDevice = SmartDevice("iPhone 13", 20, True)
print(smartDevice.getInfo())