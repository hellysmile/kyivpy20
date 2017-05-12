import os

os.environ['PYTHONASYNCIODEBUG'] = '1'

import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def main(*, loop):
    try:
        print(0)
        await asyncio.sleep(2, loop=loop)
        print(1)
    except asyncio.CancelledError:
        print(2)
        await asyncio.sleep(2, loop=loop)
        print(3)


if __name__ == '__main__':
    asyncio.set_event_loop(None)

    loop = asyncio.new_event_loop()
    loop.set_debug(True)

    try:
        coro = main(loop=loop)
        shield = asyncio.shield(coro, loop=loop)
        loop.run_until_complete(asyncio.sleep(1.1, loop=loop))
        shield.cancel()
        # loop.run_until_complete(shield)
    finally:
        loop.call_soon(loop.stop)
        loop.run_forever()
        loop.close()
