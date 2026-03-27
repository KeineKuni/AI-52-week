import requests

# 1. 定義目標網址 (這是一個提供測試資料的 API)
url = "https://jsonplaceholder.typicode.com/todos/1"

# 2. 發送 GET 請求
response = requests.get(url)

# 3. 解析回傳的 JSON 資料
data = response.json()

print(data)
