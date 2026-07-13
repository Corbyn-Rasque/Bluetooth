class Account:
    guid:           bytes
    ltk:            bytes

    def __init__(self, guid: bytes, ltk: bytes):
        self.guid = guid
        self.ltk  = ltk

class Dyson:
    product:        str
    serial:         str
    firmware:       str
    account:        Account