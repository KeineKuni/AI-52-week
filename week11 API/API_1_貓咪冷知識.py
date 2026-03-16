import requests

# 1. 定義 API 的地址（這是一個回傳隨機貓咪事實的 API）
url = "https://catfact.ninja/fact"

# 2. 發送 GET 請求
response = requests.get(url)

# 3. 檢查是否成功 (200 代表 OK)
if response.status_code == 200:
    # 4. 將 JSON 資料轉換為 Python 字典
    data = response.json()
    print(f"貓咪冷知識：{data['fact']}")
else:
    print("請求失敗！")
