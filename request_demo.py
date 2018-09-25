
import requests

url="http://api.github.com/search/repositories?q=language:python&sort=starts"

r=requests.get(url)

print("status_code",r.status_code)
json_data=r.json()

print(json_data)



