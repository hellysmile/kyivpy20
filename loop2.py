import asyncio

asyncio.set_event_loop(None)


loop = asyncio.new_event_loop()


async def coro():
    return asyncio.get_event_loop()


runnin_loop = loop.run_until_complete(coro())


assert runnin_loop is loop


# from asyncio_monkey import patch_all  # noqa isort:skip
# patch_all()  # noqa isort:skip
