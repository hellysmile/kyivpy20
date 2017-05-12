import os

os.environ['PYTHONASYNCIODEBUG'] = '1'

import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def main(*, loop):
    try:
        await asyncio.sleep(2, loop=loop)
        print(1)
    except asyncio.CancelledError:
        await asyncio.sleep(2, loop=loop)
        print(2)


if __name__ == '__main__':
    asyncio.set_event_loop(None)

    loop = asyncio.new_event_loop()
    loop.set_debug(True)

    try:
        coro = main(loop=loop)
        task = asyncio.ensure_future(coro, loop=loop)
        loop.run_until_complete(asyncio.sleep(1, loop=loop))
        task.cancel()
        loop.run_until_complete(task)
    finally:
        loop.call_soon(loop.stop)
        loop.run_forever()
        loop.close()
