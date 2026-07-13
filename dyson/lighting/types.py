from enum import IntEnum
from typing import TypeAlias, Any

from dyson.bluetooth.framing import Frames

ENDIAN = "little"

Lumens:     TypeAlias = int
Kelvin:     TypeAlias = int
Degrees:    TypeAlias = int

class Switch (IntEnum):
    ON  = 0x01
    OFF = 0x00


class Incoming:
    header: bytes = b""
    length: int

    @classmethod
    def parse(cls, payload: bytes) -> Any:
        raise NotImplementedError(payload)
    
    @classmethod
    def decode(cls, payload: bytes) -> Any:
        body = payload[len(cls.header):] if cls.header else payload
        return cls.parse(body)
    
class Outgoing:
    header: bytes = b""
    length: int

    @classmethod
    def assemble(cls, payload) -> bytes:
        raise NotImplementedError(payload)

    @classmethod
    def encode(cls, payload) -> list[bytes]:
        return Frames.pack(cls.header + cls.assemble(payload))