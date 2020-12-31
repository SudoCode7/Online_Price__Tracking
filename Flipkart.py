'''
THIS PROGRAM CHECKS THE PRODUCT PRICE EVERY 8 HRS ON FLIPKART
ENTER THE FOLLOWING FIELDS WHEREVER COMMENTED
THIS PROGRAM CHECKS 3TIMES FOR WHATEVER TIME PERIOD IS ENTERED
'''
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Samsung-Galaxy-Lite-Wi-Fi-only-Oxford/dp/B089H13XX8/ref=sr_1_4?_encoding=UTF8&dchild=1&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_r=GDW5EN7QC1NQ6K1F4WYW&pf_rd_t=36701&qid=1608895419&smid=A14CZOWI0VEHLG&sr=8-4" #ENTER URL OF THE PRODUCT
#ENTER YOUR USER AGENT BELOW, IF NOT SURE, SURF 'MY USER AGENT' ON GOOGLE
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"}
PRICE_VALUE_WANTED = 26999
EMAIL_ADDRESS = "jakshat70@gmail.com" #ENTER YOUR EMAIL ADDRESS

page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('div', attrs={'class':'_3wU53n'})
try:
    price1 = soup.find(id='priceblock_dealprice').get_text().strip()[0:-3]
except:
    price1 = soup.find(id='priceblock_ourprice').get_text().strip()[0:-3]
price1= price1[2:]
len1 = len(price1)

def trackPrices():
    price = float(Display_Price())
    if price > PRICE_VALUE_WANTED:
        diff = int(price - PRICE_VALUE_WANTED)
        print(f"Still Rs{diff} too expensive\n\n")
    else:
        print("Cheaper! Notifying...")
        sendEmail()
    pass

def Display_Price():
    print(title)
    try:
        price = soup.find(id='priceblock_ourprice').get_text().strip()[2:-3]
    except:
        price = soup.find(id='priceblock_dealprice').get_text().strip()[2:-3]
    print(price)
    price12 = ''
    if len1==6:
        price12 = price[0:2]+price[3:]
    elif len1 == 5:
        price12 = price[0:1] + price[3:]
    else:
        try:
            price1 = soup.find(id='priceblock_dealprice').get_text().strip()[2:-3]
        except:
            price1 = soup.find(id='priceblock_ourprice').get_text().strip()[2:-3]
        price12 = price
    return price12

def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+title+"- Rs"+price1+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587) #IF USING GOOGLE, DONT TOUCH THIS FIELD
    server.ehlo()                                          #ELSE SURF FOR REQUIRED EMAIL SERVIVE AND IT'S PORT
    server.starttls()
    server.login(EMAIL_ADDRESS, 'Shailendrajain')#ENTER EMAIL ID PASSWORD IN QUOTES GIVEN
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print('Email Sent!\n\n')
    pass

if __name__ == "__main__":
    n=0
    while n!=3:
        trackPrices()
        time.sleep(60)#ENTER TIME TO CHECK AFTER HERE IN ROUND BRACKETS IN SECONDS
        n+=1