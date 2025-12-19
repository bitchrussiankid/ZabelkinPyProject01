class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def takePhoto(self):
        return f"Photo taken, resolution: {self.resolution} MP"


class GPS:
    def __init__(self, hasGps: bool):
        self.hasGps = hasGps

    def getLocation(self):
        if self.hasGps:
            return "Coordinates received"
        else:
            return "GPS not available"


class SmartCamera(Camera, GPS):
    def __init__(self, resolution, hasGps, brand, model):
        Camera.__init__(self, resolution)
        GPS.__init__(self, hasGps)
        self.brand = brand
        self.model = model

    def deviceInfo(self):
        return f"{self.brand} {self.model} with {self.resolution} megapixel camera"

smartCamera = SmartCamera(resolution = 108, hasGps = True, brand = "Canon", model = "EOS 250D")
print(smartCamera.deviceInfo())