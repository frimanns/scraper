import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/dp/B07B4L1PQ8?aaxitk=CSf1VNHhnB4lvo6MBWJs2g&pd_rd_i=B07B4L1PQ8&pf_rd_p=bcd6e1ba-4fe0-4969-b1b9-89f89ee75b1b&hsa_cr_id=3743975120502&sb-ci-n=productDescription&sb-ci-v=Sony%20Alpha%207M3%20E-Mount%20Vollformat%20Digitalkamera%20ILCE-7M3%20(24%2C2%20Megapixel%2C%207%2C6cm%20(3%20Zoll)%20Touch-Display%2C%20Exmor%20R%20CMOS%20Vollformatsensor%2C%20XGA%20OLED%20Sucher%2C%202%20Kartenslots%2C%20nur%20Geh%C3%A4use)%20schwarz'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if (converted_price < 1.700):
        send_mail()

    print(converted_price)
    print (title.strip())
