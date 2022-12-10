import webbrowser
import random
import time

while True:
    sites_list = ["http://google.com" , "http://facebook.com" , "http://youtube.com"]
    rand_site = random.choice(sites_list)
    webbrowser.open(rand_site)
    seconds = random.randrange(5, 10)
    time.sleep(seconds)