import asyncio
from jikanpy import AioJikan

async def main():
    async with AioJikan() as aio_jikan:
        mushishi = await aio_jikan.anime(457)
        fma = await aio_jikan.manga(25)
    # You can also construct AioJikan like below, but make sure to close the object
    aio_jikan_2 = AioJikan()
    print(mushishi)
    print(fma)
    await aio_jikan_2.close()

asyncio.run(main())