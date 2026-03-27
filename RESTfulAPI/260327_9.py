import requests

api_key = "你的_API_KEY_在這裡"
url = "https://api.example.com/v1/completions"  # 這是假設的 AI API 網址

# 1. 設定 Headers (身分驗證)
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

# 2. 設定要傳送給 AI 的內容
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "請幫 VitaTiere 品牌寫一段貓用益生菌的廣告詞"}
    ],
}

# 3. 發送請求
# response = requests.post(url, headers=headers, json=payload)
