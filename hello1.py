import asyncio
from aiohttp import web


async def hello(request):
    fut = asyncio.Future()
    await fut
    return web.Response(text='Hello, world')


app = web.Application()
app.router.add_get('/', hello)

if __name__ == '__main__':
    import os
    print(os.getpid())
    web.run_app(app, shutdown_timeout=1, port=8000)
    print('Done')
