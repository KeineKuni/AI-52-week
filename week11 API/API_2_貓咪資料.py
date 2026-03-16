import requests

# 使用一個更穩定的 API (貓咪資料)
url = "https://api.thecatapi.com/v1/breeds"

try:
    # 1. 發送請求
    response = requests.get(url, timeout=10)  # 設定超時，避免無限等待

    # 2. 檢查狀態碼 (200 代表 OK)
    if response.status_code == 200:
        data = response.json()
        # 取得第一筆品種資料
        first_cat = data[0]
        print(f"🐈 找到品種：{first_cat['name']}")
        print(f"🌟 性格特徵：{first_cat['temperament']}")
    else:
        print(f"⚠️ 請求失敗，錯誤碼：{response.status_code}")

except Exception as e:
    # 3. 處理如「網址掛了」或「沒網路」等例外狀況
    print(f"❌ 發生錯誤：{e}")
