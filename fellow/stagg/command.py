#! python3
from __future__ import annotations

from fellow.stagg.state import State, Switch, Degrees

class Command:
    HEADER:     bytearray = bytearray(b'\xef\xdd')
    COMMAND:    bytearray = bytearray(b'\x0a')
    id:         bytearray

    @classmethod
    def checksum(cls, sequence: bytearray, value: bytearray) -> bytearray:
        return bytearray([(sum(sequence) + sum(value)) & 0xFF])

    @classmethod
    def encode(cls, state: State, value) -> bytearray:
        message = cls.HEADER + cls.COMMAND + state.sequence + value
        state.sequence[0] += 1
        return message

class Power (Command):
    id = bytearray([0x00])

    @classmethod
    def encode(cls, state: State, value: Switch) -> bytearray:
        message = cls.id + \
                  bytearray([value]) + \
                  cls.checksum(state.sequence, bytearray([value])) + \
                  cls.id
        return super().encode(state, message)

class Temperature (Command):
    id = bytearray([0x01])

    @classmethod
    def encode(cls, state: State, value: Degrees) -> bytearray:
        message = cls.id + \
                  bytearray(value.to_bytes(2)) + \
                  cls.checksum(state.sequence, bytearray(value.to_bytes(2))) + \
                  cls.id
        return super().encode(state, message)