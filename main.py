import asyncio
import json
import aiohttp

TOKEN = "NTE2NTk0ODMzMjg1MDU0NDY0.Dt1-Rg.Ip3jNseffENgmnOzmDefui1pN8I"
URL = "https://discordapp.com/api"
async def api_call(path):
    """Return the JSON body of a call to Discord REST API."""
    with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}{path}") as response:
            assert 200 == response.status, response.reason
            return await response.json()
async def main():
    """Main program."""
    response = await api_call("/gateway")
    print(response)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()