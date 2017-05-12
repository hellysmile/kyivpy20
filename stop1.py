import asyncio


async def main(*, loop):
    print(1)


if __name__ == '__main__':
    asyncio.set_event_loop(None)

    loop = asyncio.new_event_loop()

    loop.run_until_complete(main(loop=loop))
    loop.close()
