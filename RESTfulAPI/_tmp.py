import requests, random


r = random.randint(1, 100)


# 1. 定義目標網址 (這是一個提供測試資料的 API)
url = f"https://jsonplaceholder.typicode.com/todos/{r}"

# 2. 發送 GET 請求
response = requests.get(url)

# 3. 解析回傳的 JSON 資料
data = response.json()

print(f"{r}\n{data}")
