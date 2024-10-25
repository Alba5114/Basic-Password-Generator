import random
import time

words = ("qwertyuopasdfhjklizxcvbnmQWERTYUIOPASDFGHJLZXCVBNM1234567890#!?=()\/*")
password = ""

print("------------------------------------")

length = int(input("Enter password length : "))
for i in range(length):
    password = password + random.choice(words)

print("Generating password...")
time.sleep(0.9)
print("Password generated")
time.sleep(0.2)
print("Password : " + password)
