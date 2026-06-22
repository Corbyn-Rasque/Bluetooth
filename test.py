#! python3

from fellow.stagg.ekg import Kettle

import asyncio

async def main():
    kettle = Kettle()
    kettles = await kettle.scan()

    _, address = next(iter(kettles.items()))

    if address:
        await kettle.connect(address)

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await kettle.connection.disconnect()

asyncio.run(main())