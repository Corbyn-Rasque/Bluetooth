from dyson.bluetooth.framing import Frames

class Collector:
    expected:   int
    buffer:     bytearray

    def __init__(self, length: int):
        self.expected   = Frames.length(length)
        self.buffer     = bytearray()
    
    def feed(self, chunk: bytes) -> bytes | None:
        self.buffer += chunk

        if len(self.buffer) < self.expected:
            return None

        if len(self.buffer) > self.expected:
            raise ValueError("Received more data than expected for this message")

        raw = bytes(self.buffer)
        self.buffer.clear()
        return Frames.unpack(raw)