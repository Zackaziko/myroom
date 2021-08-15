import requests
print("please enter the name to be predicted")
name = str(input())
link = "https://api.genderize.io/?name="+name
page = requests.get(link)
print(page.text)
