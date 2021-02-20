'''
THIS PROGRAM CHECKS THE PRODUCT PRICE EVERY x(time entered by you) HRS ON FLIPKART.
THIS PROGRAM CHECKS 3 TIMES FOR WHATEVER TIME PERIOD IS ENTERED.
'''
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from mailjet_rest import Client
import os
api_key = '1234567890SJHq8h38'  # Enter your api key here
api_secret = 'Sahu2kluovselrh'  # Enter your api secret key here
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
URL = input("Enter the product URL= ")
time_period = int(input("Enter the number of hours, you want the price to be checked in= "))
print("\n")
PRICE_VALUE_WANTED = float(input("What price do you expect? "))  # ENTER THE PRICE VALUE YOU WANT TO BE CHECKED
print("\n")
EMAIL_ADDRESS = input("Enter your gmail address ")  # ENTER YOUR EMAIL ADDRESS
print("\n")
response = requests.get(URL)
page = response.text
soup = BeautifulSoup(page, 'html.parser')
name = soup.findAll('h1', class_="yhB1nd")
title = name[0].get_text()
price = soup.findAll('div', class_='_30jeq3 _16Jk6d')
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
    mailtext = str(title1) + '- Rs' + price12 + '\n'  # RS CAN BE CHANGED TO YOUR CURRENCY
    data = {
        'Messages': [
            {
                "From": {
                    "Email": EMAIL_ADDRESS,
                    "Name": "Sudo" #Enter your name here
                },
                "To": [
                    {
                        "Email": EMAIL_ADDRESS,
                        "Name": "Sudo" #Enter your name here
                    }
                ],
                "Subject": subject,
                "TextPart": mailtext,
                "HTMLPart": URL,
                "CustomID": "Flipkart_Price_Tracker"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())
    pass
if __name__ == "__main__":
    n = 0
    while n != 3:
        trackPrices()
        time.sleep(time_period * 60 * 60)  # ENTER TIME TO CHECK, HERE IN ROUND BRACKETS IN SECONDS
        n += 1
