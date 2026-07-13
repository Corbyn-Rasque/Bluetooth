from dyson.bluetooth.collector                              import Collector
from dyson.lighting.solarcycle.protocol.messages.data       import MESSAGES
from dyson.lighting.solarcycle.protocol.messages.commands   import COMMANDS

class Data:
    def __init__(self):
        self.collectors = {uuid: Collector(msg.length) for uuid, msg in MESSAGES.items()}

    def on_notify(self, uuid: str, chunk: bytes):
        if (raw := self.collectors[uuid].feed(chunk)) is None:
            return None
        return MESSAGES[uuid].decode(raw)

    def write(self, uuid: str, value) -> list[bytes]:
        return COMMANDS[uuid].encode(value)