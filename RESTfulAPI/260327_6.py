import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {"userId": 1}

# 2. 發送請求並加入 params
response = requests.get(url, params=payload)

# 3. 如果成功，印出第一筆資料的標題
if response.status_code == 200:
    data = response.json()
    print(data[0]["title"])
