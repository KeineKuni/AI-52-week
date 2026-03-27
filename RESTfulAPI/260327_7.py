import requests

url = "https://jsonplaceholder.typicode.com/posts"

# 1. 準備要新增的資料
new_post = {
    "title": "VitaTiere 貓用益生菌",
    "body": "這是一筆測試訂單內容",
    "userId": 1,
}

# 2. 發送 POST 請求
response = requests.post(url, json=new_post)

# 3. 檢查結果
if response.status_code == 201:  # 201 代表 "Created" (已建立)
    print("成功新增資料！")
    print(response.json())
