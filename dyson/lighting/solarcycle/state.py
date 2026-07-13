from dyson.lighting.types import Lumens, Kelvin, Degrees, Switch

class Light:
    power:          Switch  | None = None
    brightness:     Lumens  | None = None
    temperature:    Kelvin  | None = None

class Mode:
    cycle:          Switch  | None = None
    motion:         Switch  | None = None
    automatic:      Switch  | None = None

class Sensor:
    motion:         bool    | None = None
    brightness:     Lumens  | None = None
    temperature:    Degrees | None = None

class State:
    light:          Light
    mode:           Mode
    sensor:         Sensor
    
    authenticated:  bool

    def __init__(self):
        self.light          = Light()
        self.mode           = Mode()
        self.sensor         = Sensor()
        self.authenticated  = False