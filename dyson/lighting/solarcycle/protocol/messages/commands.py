from dyson.lighting.types import Outgoing, Lumens, Kelvin, Degrees, Switch, ENDIAN
from dyson.lighting.solarcycle.protocol.services import Data

class Power (Outgoing):
    length = 1

    @classmethod
    def assemble(cls, payload: Switch) -> bytes:
        return bytes([payload])
    
class Brightness (Outgoing):
    length = 2

    @classmethod
    def assemble(cls, payload: Lumens) -> bytes:
        return payload.to_bytes(cls.length, ENDIAN)
    
class Temperature (Outgoing):
    length = 2

    @classmethod
    def assemble(cls, payload: Kelvin) -> bytes:
        return payload.to_bytes(cls.length, ENDIAN)

class Motion (Outgoing):
    length = 1

    @classmethod
    def assemble(cls, payload: Switch) -> bytes:
        return bytes([payload])
    
class Automatic (Outgoing):
    length = 1

    @classmethod
    def assemble(cls, payload: Switch) -> bytes:
        return bytes([payload])
    
COMMANDS: dict[str, Outgoing] = {
    Data.Characteristic.POWER:       Power(),
    Data.Characteristic.BRIGHTNESS:  Brightness(),
    Data.Characteristic.TEMPERATURE: Temperature(),
    Data.Characteristic.MOTION:      Motion(),
    Data.Characteristic.AUTOMATIC:   Automatic(),
}