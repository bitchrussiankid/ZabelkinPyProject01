class SmartDevice:
    def __init__(self, deviceId: str, status = "off"):
        self.deviceId = deviceId
        self.status = status

    def toggleStatus(self):
        if self.status == "off":
            self.status = "on"
        else:            
            self.status = "off"
        return self.status

    def getInfo(self):
        return f"Device {self.deviceId} is {self.status}"


class SmartLight(SmartDevice):
    def __init__(self, deviceId, brightness = 50):
        super().__init__(deviceId)
        self.brightness = brightness
        self.maxBrightness = 100

    def minBrightness(minimum = 50):
        def decorator(func):
            def wrapper(*args):

                if args[1] < minimum:
                    print(f"Warning! Brightness below minimum allowed ({minimum}). Set to {minimum}.")
                    func(args[0], minimum)
                else:
                    func(*args)
            return wrapper
        return decorator

    @minBrightness(70)
    def changeBrightness(self, value):
        if value <= self.maxBrightness:
            self.brightness = value
        else:
            print(f"Warning! Brightness is above the maximum allowed ({self.maxBrightness}). Set to {self.maxBrightness}.")
            self.brightness = self.maxBrightness

    def getInfo(self):
        return f"Light {self.deviceId} is {self.status} with brightness {self.brightness}/{self.maxBrightness}"



smartLight1 = SmartLight("ARM1010", 70)
print(smartLight1.getInfo())
smartLight1.toggleStatus()


smartLight1.changeBrightness(80)
print(smartLight1.getInfo())

smartLight1.changeBrightness(110)
print(smartLight1.getInfo())

    