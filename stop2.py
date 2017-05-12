import asyncio


async def main(*, loop):
    print(1)


if __name__ == '__main__':
    asyncio.set_event_loop(None)

    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(main(loop=loop))
    finally:
        loop.call_soon(loop.stop)
        loop.run_forever()
        loop.close()
