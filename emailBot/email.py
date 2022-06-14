# -*- coding: cp1252 -*-
import requests
import random
import time
import smtplib
import os

from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

url = "https://twitter135.p.rapidapi.com/Search/"

querystring = {"q":"dream smp","count":"20","tweet_search_mode":"live"}

headers = {
	"X-RapidAPI-Host": "twitter135.p.rapidapi.com",
	"X-RapidAPI-Key": "cadd600414mshd4b4ff5b2e67303p127fb5jsn8176d849345a"
}

while(True):
    response = requests.request("GET", url, headers=headers, params=querystring)
    keylist = list(response.json()["globalObjects"]["tweets"].keys())
    key = keylist[random.randint(0, len(keylist)-1)]

    gmail_user = 'ilovedreamsmp9@gmail.com'
    gmail_password = PASSWORD

    sent_from = gmail_user
    to = ['wella123badr@gmail.com', 'seannoh@gmail.com']
    subject = 'dream smp updates'
    body = response.json()["globalObjects"]["tweets"][key]["full_text"]

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong�",ex)

    time.sleep(30)
