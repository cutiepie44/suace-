import time
import webbrowser
print("suace+")
code = input("whats the code ")
website = "https://nhentai.net/g/"
print(website + code)   
webbrowser.open(f"{website}{code}")
time.sleep (5)
