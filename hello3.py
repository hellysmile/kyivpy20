# import asyncio
# import logging

# from aiohttp import web


# async def hello(request):
#     # try:
#     #     print(1)
#     #     await asyncio.sleep(5)
#     #     print(2)
#     # except asyncio.CancelledError:
#     #     print(3)
#     #     await asyncio.sleep(1)
#     #     print(4)

#     async def _inline():
#         print(1)
#         await asyncio.sleep(10)
#         print(2)

#     await asyncio.shield(_inline())

#     return web.Response(text='Hello, world')


# app = web.Application()
# app.router.add_get('/', hello)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)

#     web.run_app(app, shutdown_timeout=1, port=8000)

# ##########

import asyncio
import logging

from aiohttp import web

from async_armor import armor


async def hello(request):
    @armor
    async def _inline():
        print(1)
        await asyncio.sleep(10)
        print(2)

    await _inline()

    return web.Response(text='Hello, world')


app = web.Application()
app.router.add_get('/', hello)
async def close_armor(app):
    armor.close()
    await armor.wait_closed()
# app.on_cleanup.append(close_armor)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app, shutdown_timeout=1, port=8000)
