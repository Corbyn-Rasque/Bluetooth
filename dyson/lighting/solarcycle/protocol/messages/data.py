from dyson.lighting.types import Incoming, Lumens, Kelvin, Degrees, Switch, ENDIAN
from dyson.lighting.solarcycle.protocol.services import Data

    
class Power (Incoming):
    length = 1

    @classmethod
    def parse(cls, payload: bytes) -> Switch:
        return Switch(payload[0])

class Brightness (Incoming):
    length = 2

    @classmethod
    def parse(cls, payload: bytes) -> Lumens:
        return Lumens.from_bytes(payload, ENDIAN)

class Temperature (Incoming):
    length = 2

    @classmethod
    def parse(cls, payload: bytes) -> Kelvin:
        return Kelvin.from_bytes(payload, ENDIAN)
    
class Motion (Incoming):
    length = 1

    @classmethod
    def parse(cls, payload: bytes) -> Switch:
        return Switch(payload[0])

class Automatic (Incoming):
    length = 1

    @classmethod
    def parse(cls, payload: bytes) -> Switch:
        return Switch(payload[0])

class SensorBrightness (Incoming):
    length = 2

    @classmethod
    def parse(cls, payload: bytes) -> int:
        return int.from_bytes(payload, ENDIAN)

MESSAGES: dict[str, Incoming] = {
    Data.Characteristic.POWER:         Power(),
    Data.Characteristic.BRIGHTNESS:    Brightness(),
    Data.Characteristic.TEMPERATURE:   Temperature(),
    Data.Characteristic.MOTION:        Motion(),
    Data.Characteristic.AUTOMATIC:     Automatic(),
    Data.Characteristic.SENS_BRIGHT:   SensorBrightness()
}