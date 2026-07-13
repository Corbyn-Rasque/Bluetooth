from __future__ import annotations
from typing import Iterator

LIMIT   = 20
HEADER  = 1
DATA    = LIMIT - HEADER

TYPE  = 0x8

def chunk(data: bytes) -> Iterator[bytes]:
    for i in range(0, len(data), DATA):
        yield data[i : i + DATA]

class Frames:
    @classmethod
    def pack(cls, data: bytes) -> list[bytes]:
        if len(data) < LIMIT:
            return [data]

        chunks  = [*chunk(data)]
        count   = len(chunks)

        # Type & message chunk count (less the first message) in same header byte
        start   = [ bytes([(TYPE << 4) | ((count - 1) & 0x0F)]) + chunks[0]      ]
        rest    = [ bytes([i + 1]) + chunk for i, chunk in enumerate(chunks[1:]) ]

        return start + rest

    @classmethod
    def unpack(cls, data: bytes) -> bytes:
        if len(data) < LIMIT:
            return data

        header = data[0]
        type_nibble = (header >> 4) & 0x0F
        count_nibble = header & 0x0F

        if type_nibble != TYPE:
            raise ValueError(f"unexpected frame type: {type_nibble:#x}")

        total = count_nibble + 1
        payloads: dict[int, bytes] = {}

        for i in range(total):
            start = i * LIMIT
            frame = data[start : ] if i == total - 1 else data[start : start + LIMIT]

            idx = 0 if i == 0 else frame[0]
            payloads[idx] = frame[1:]

        if len(payloads) != total:
            raise ValueError("missing frame(s)")

        return b"".join(payloads[i] for i in range(total))
    
    @classmethod
    def length(cls, length: int) -> int:
        if length < LIMIT:
            return length
        
        count = (length + DATA - 1) // DATA
        return length + count