'''
THIS PROGRAM CHECKS THE PRODUCT PRICE EVERY 8 HRS ON AMAZON.
ENTER THE FOLLOWING FIELDS WHEREVER COMMENTED........
THIS PROGRAM CHECKS 3 TIMES FOR WHATEVER TIME PERIOD IS ENTERED.
'''
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter the product URL= ")
# print("\n")
time_period = int(input("Enter the number of hours, you want the price to be checked in= "))
print("\n")
agent = input("Enter your brower agent, if you are not aware of that just GOOGLE 'My User Agent', while I wait............")
print("\n")
# YOUR USER AGENT, IF NOT SURE, SURF 'MY USER AGENT' ON GOOGLE
HEADERS = {"User-Agent": agent}
PRICE_VALUE_WANTED = float(input("What price do you except? "))  # THE PRICE VALUE YOU WANT TO BE CHECKED
print("\n")
EMAIL_ADDRESS = input("Enter your gmail address ")  # YOUR EMAIL ADDRESS
print("Lastly enter your password, don't worry it's not going to be used anywhere and will only")
Password = input("be used by the bot to login on your behalf(Don't believe me, check the code yourself :-))   ")
print("\n")
page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id='productTitle').get_text().strip()
try:
    price1 = soup.find(id='priceblock_dealprice').get_text().strip()[0:-3]
except:
    price1 = soup.find(id='priceblock_ourprice').get_text().strip()[0:-3]
price1 = price1[2:]


# len1 = len(price1)

def trackPrices():
    price = float(Display_Price())
    if price > PRICE_VALUE_WANTED:
        diff = int(price - PRICE_VALUE_WANTED)
        print(f"Still Rs{diff} too expensive\n\n")  # RS CAN BE CHANGED TO YOUR CURRENCY
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
    len1 = len(price)
    if len1 == 6:
        price12 = price[0:2] + price[3:]
    elif len1 == 5:
        price12 = price[0:1] + price[2:]
    else:
        price12 = price
    return price12


def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext = 'Subject:' + subject + '\n\n' + title + '"- Rs' + price1 + '\n' + URL  # RS CAN BE CHANGED TO YOUR CURRENCY
    title1 = title.encode('utf-8')
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  # IF USING GOOGLE, DON'T TOUCH THIS FIELD OR ELSE
    server.ehlo()                                           # SURF FOR REQUIRED EMAIL SERVICE AND IT'S PORT
    server.starttls()
    server.login(EMAIL_ADDRESS, Password)  # EMAIL-ID PASSWORD IN DOUBLE QUOTES GIVEN
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print('Email Sent!\n\n')
    pass


if __name__ == "__main__":
    n = 0
    while n != 3:
        trackPrices()
        time.sleep(time_period * 60 * 60)  # ENTER TIME TO CHECK, HERE IN ROUND BRACKETS IN SECONDS
        n += 1


