import requests
response=requests.get("https://books.toscrape.com/")
if response.ok:
    print(response.text)
else:
    print("请求失败")