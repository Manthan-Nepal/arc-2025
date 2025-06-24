import httpx
import asyncio

r = httpx.get('https://httpbin.org/get')

data = {'username': 'bhumika', 'password': '123'}
r = httpx.post('https://httpbin.org/post', data=data)


print(r.status_code)      


#same connection
with httpx.Client() as client:
    r= client.get("https://example.com")
    r2 = client.get("https://example.com")

print(r.status_code)

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com")
        print(response)

asyncio.run(main())
