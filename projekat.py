import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.winwin.rs/pc-periferije-monitori/slusalice-i-mikrofoni/bubice-sa-mikrofonom-altec-lansing-free-bluetooth-8661608.html'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

def proveri_cenu():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    titl = soup.find(itemprop="name").get_text()
    cena = soup.find(itemprop="price").get_text()
    konvertovana_cena = float(cena[0:6])

    if(konvertovana_cena < 1.7):
        posalji_mejl()

    print(titl)
    print(konvertovana_cena)

    if(konvertovana_cena > 1.7):
        posalji_mejl()

def posalji_mejl():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('cipovicbojan607@gmail.com', 'exiixgfareatlrgg')

    subject = 'Price dropped'
    body = 'Proveri sajt! https://www.winwin.rs/bubice-sa-mikrofonom-altec-lansing-free-bluetooth-8661608.html'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'randomemail@hotmail.rs',
        msg
    )
    print('Email is sent!')
    server.quit()

while(True):
    proveri_cenu()
    time.sleep(86400)