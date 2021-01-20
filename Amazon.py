'''
THIS PROGRAM CHECKS THE PRODUCT PRICE EVERY 8 HRS ON AMAZON.
ENTER THE FOLLOWING FIELDS WHEREVER COMMENTED........
THIS PROGRAM CHECKS 3 TIMES FOR WHATEVER TIME PERIOD IS ENTERED.
'''
import requests
from bs4 import BeautifulSoup
from mailjet_rest import Client
import time
api_key = '' #Enter your api key here
api_secret = '' #Enter your api secret here
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
URL = input("Enter the product URL= ")
time_period = int(input("Enter the number of hours, you want the price to be checked in= "))
print("\n")
PRICE_VALUE_WANTED = float(input("What price do you except? "))  # ENTER THE PRICE VALUE YOU WANT TO BE CHECKED
print("\n")
EMAIL_ADDRESS = input("Enter your gmail address ")  # ENTER YOUR EMAIL ADDRESS
page = requests.get(URL)
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
            title1 = title.encode('utf-8')
            mailtext = str(title1[2:]) + ' - Rs' + price1 + '  \n->' + URL  # RS CAN BE CHANGED TO YOUR CURRENCY
            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": EMAIL_ADDRESS,
                            "Name": "Sudo"
                        },
                        "To": [
                            {
                                "Email": EMAIL_ADDRESS,
                                "Name": "Sudo"
                            }
                        ],
                        "Subject": subject,
                        # "TextPart": mailtext,
                        "HTMLPart": mailtext + URL,
                        "CustomID": "Flipkart_Price_Tracker"
                    }
                ]
            }
            result = mailjet.send.create(data=data)
            print(result.status_code)
            print(result.json())
            print('Email Sent!\n\n')
            pass

if __name__ == "__main__":
            n = 0
            while n != 3:
                trackPrices()
                time.sleep(time_period * 60 * 60)  # ENTER TIME TO CHECK, HERE IN ROUND BRACKETS IN SECONDS
                n += 1
