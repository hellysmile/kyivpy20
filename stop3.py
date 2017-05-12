import os

os.environ['PYTHONASYNCIODEBUG'] = '1'

import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def main(*, loop):
    print(1)


if __name__ == '__main__':
    asyncio.set_event_loop(None)

    loop = asyncio.new_event_loop()
    loop.set_debug(True)

    try:
        main(loop=loop)
        fut = asyncio.Future(loop=loop)
        fut.set_result(None)
    finally:
        loop.call_soon(loop.stop)
        loop.run_forever()
        loop.close()
