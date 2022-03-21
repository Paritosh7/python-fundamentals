import requests

r = requests.get("https://api.github.com/search/users",{
    "q" : "q",
    "sort" : "followers",
    "per_page" : 2
})
if r.status_code == 200:
    data = r.json()
    print(data)