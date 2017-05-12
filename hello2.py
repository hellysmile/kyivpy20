import asyncio
import signal
from aiohttp import web


async def hello(request):
    fut = asyncio.Future()
    await fut
    return web.Response(text='Hello, world')


app = web.Application()
app.router.add_get('/', hello)

if __name__ == '__main__':
    import os

    pid = os.getpid()

    print(pid)

    def _sigint(signum, frame):
        os.kill(pid, signal.SIGINT)

    signal.signal(signal.SIGTERM, _sigint)

    web.run_app(app, shutdown_timeout=1, port=8000)
    print('Done')
