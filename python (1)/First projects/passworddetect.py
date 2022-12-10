import random
#import pyautogui as auto
import time

while True:

    def getpassword(data):
        max = 6
        password = ""
        while len(password) != max:
            value = random.choice(data)
            password += value
        return password

    data = '1234567890'
    
    print(getpassword(data))
    
#    while True:
#        auto.write(getpassword(data))
#        auto.press('enter')
#        time.sleep(1)
 #		print(getpassword(data))