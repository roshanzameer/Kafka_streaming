import json
import requests
import pandas as pd

urls = [
  "https://reqres.in/api/users?page=1",
"https://reqres.in/api/users?page=2",
"https://reqres.in/api/users?page=3",
"https://reqres.in/api/users?page=4"]

response = []
for url in urls:
    response.append(json.loads(requests.get(url).content.decode('utf-8')))

user_data = []
for data in response:
    for i in data['data']:
        user_data.append(i)

df = pd.DataFrame(user_data)
df.to_csv('user_data.csv', index=False)




print(user_data)





