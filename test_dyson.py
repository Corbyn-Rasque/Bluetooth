import asyncio, os, time
from time import sleep

from dyson.product import Account
from dyson.lighting.solarcycle.lamp import Lamp

from dotenv import load_dotenv

load_dotenv()

GUID = os.getenv('GUID') or ""
LTK  = os.getenv('LTK') or ""

NAME = os.getenv('NAME') or ""

async def main():
    account = Account(
    guid=bytes.fromhex(GUID.replace("-", "")),
    ltk=bytes.fromhex(LTK),
)

    lamp = Lamp(account)

    devices = await lamp.connection.scan(NAME)

    if not devices:
        raise RuntimeError(f'"{NAME}" not found.')

    device = devices[0]


    # print(f"Connecting to {device.name} ({device.address})")

    start = time.time()
    await lamp.connect(device)
    end = time.time()

    print(f"{end - start:0.1f}", 'seconds')

    # print("Authenticated:", lamp.state.authenticated)

    switch = False
    while(True):
        await lamp.power(switch)
        switch = not switch
        sleep(1)

    await lamp.connection.disconnect()


if __name__ == "__main__":
    asyncio.run(main())