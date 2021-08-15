import requests
import sys
try:
    name = sys.argv[1]
    link = "https://api.genderize.io/?name="+name
    page = requests.get(link)
    print(page.text)
except IndexError:
    print("please enter the name to be predicted")
    name2 = str(input())
    link = "https://api.genderize.io/?name="+name2
    page = requests.get(link)
    print(page.text)
