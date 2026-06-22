from fellow.stagg.state import State, Switch, Degrees, Unit

class Message:
    HEADER: bytearray = bytearray(b'\xef\xdd')
    LENGTH: int

    def parse(self, payload: bytearray, state: State):
        raise NotImplementedError

class Power (Message):
    LENGTH: int         = 2

    def parse(self, payload: bytearray, state: State):
        state.power = Switch(payload[0])

class Hold (Message):
    LENGTH: int         = 2

    def parse(self, payload: bytearray, state: State):
        state.hold = Switch(payload[0])

class Temperature (Message):
    LENGTH: int         = 4

class Target (Temperature):
    def parse(self, payload: bytearray, state: State):
        state.target = Degrees(payload[0])
        state.unit   = Unit(payload[1])

class Current (Temperature):
    def parse(self, payload: bytearray, state: State):
        state.current = Degrees(payload[0])
        state.unit    = Unit(payload[1])

class Timer (Message):
    LENGTH: int         = 2

    def parse(self, payload: bytearray, state: State):
        state.timer = int(payload[0])

class Mode (Message):
    LENGTH: int = 2

    def parse(self, payload: bytearray, state: State):
        state.mode = Switch(payload[0])

class Docked (Message):
    LENGTH: int = 2

    def parse(self, payload: bytearray, state: State):
        state.docked = Switch(payload[0])

class Unknown (Message):
    def __init__(self, length: int):
        self.LENGTH = length

    def parse(self, payload: bytearray, state: State):
        pass

MESSAGES: dict[int, Message] = {
    0x00: Power(),
    0x01: Hold(),
    0x02: Target(),
    0x03: Current(),
    0x04: Timer(),
    0x05: Unknown(4),
    0x06: Mode(),
    0x07: Unknown(3),
    0x08: Docked()
}