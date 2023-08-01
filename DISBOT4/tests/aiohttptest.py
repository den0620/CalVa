import aiohttp,json

url='https://cdn.discordapp.com/attachments/990586363608956988/990698375856934922/GOS01-Oshioki-Education-Time-Foreign-VN----6585693.gif'

async with ClientSession() as session:
    async with session.get(url, params=params) as response:
        response = await response.json()
