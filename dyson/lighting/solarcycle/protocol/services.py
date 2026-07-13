from enum import StrEnum

class Services:
    UUID = lambda number: f'2DD1{number}-1C37-452D-8979-D1B4A787D0A4'

class Handshake:
    Service         = Services.UUID("0010")

    class Characteristic(StrEnum):
        WRITE       = Services.UUID("0011")
        READ        = Services.UUID("0013")

class Control:
    Service         = Services.UUID('0020')

    class Characteristic (StrEnum):
        WRITE       = Services.UUID('0021')

class Data:
    Service         = Services.UUID('FFF0')

    class Characteristic (StrEnum):
        INTENSITY   = Services.UUID('1000')
        TEMPERATURE = Services.UUID('1001')
        SENS_BRIGHT = Services.UUID('1004')
        POWER       = Services.UUID('1005')
        AUTOMATIC   = Services.UUID('1006')
        MOTION      = Services.UUID('1007')
        BRIGHTNESS  = Services.UUID('1009')