'''
THIS PROGRAM CHECKS THE PRODUCT PRICE EVERY 8 HRS ON FLIPKART.
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
# ENTER YOUR USER AGENT BELOW, IF NOT SURE, SURF 'MY USER AGENT' ON GOOGLE
HEADERS = {"User-Agent": {agent}}
PRICE_VALUE_WANTED = float(input("What price do you except? "))  # ENTER THE PRICE VALUE YOU WANT TO BE CHECKED
print("\n")
EMAIL_ADDRESS = input("Enter your gmail address ")  # ENTER YOUR EMAIL ADDRESS
print("Lastly enter your password, don't worry it's not going to be used anywhere and will only")
Password = input("be used by the bot to login on your behalf(Don't believe me, check the code yourself :-))   ")
print("\n")
response = requests.get(URL)
page = response.text
soup = BeautifulSoup(page,'html.parser')
name = soup.findAll('h1',class_= "yhB1nd")
title = name[0].get_text()
price = soup.findAll('div',class_= '_30jeq3 _16Jk6d')
price1 = price[0].get_text()

def trackPrices():
    price = float(Display_Price())
    if price > PRICE_VALUE_WANTED:
        diff = int(price - PRICE_VALUE_WANTED)
        print(f"Still Rs{diff} too expensive\n\n")  # RS CAN BE CHANGED TO YOUR CURRENCY
    else:
        print("Cheaper! Notifying...")
        sendEmail(price)
    pass


def Display_Price():
    print(title)
    print(price1)
    len1 = len(price1)
    if len1 == 6:
        price12 = price1[1:2] + price1[3:]
    elif len1 == 7:
        price12 = price1[1:3] + price1[4:]
    else:
        price12 = price1[1:]

    return price12


def sendEmail(price12):
    subject = "Flipkart Prize Dropped!!"
    price12 = str(price12)
    title1 = title.encode('utf-8')
    mailtext = 'Subject:' + subject + '\n\n' + str(title1) + '- Rs' + price12 + '\n' + URL #RS CAN BE CHANGED TO YOUR CURRENCY
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  # IF USING GOOGLE, DON'T TOUCH THIS FIELD OR ELSE
    server.ehlo()  # SURF FOR REQUIRED EMAIL SERVICE AND IT'S PORT
    server.starttls()
    server.login(EMAIL_ADDRESS, Password)  # ENTER EMAIL-ID PASSWORD IN DOUBLE QUOTES GIVEN
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print('Email Sent!\n\n')
    pass


if __name__ == "__main__":
    n = 0
    while n != 3:
        trackPrices()
        time.sleep(time_period * 60 * 60)  # ENTER TIME TO CHECK, HERE IN ROUND BRACKETS IN SECONDS
        n += 1
