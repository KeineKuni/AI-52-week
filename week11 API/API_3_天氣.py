import requests

# 1. 定義 API 網址
url = "https://api.open-meteo.com/v1/forecast?latitude=23.035689&longitude=120.277551&current_weather=true"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # 2. 解析層層嵌套的字典
        current = data["current_weather"]
        temp = current["temperature"]
        wind = current["windspeed"]

        print(f"📍 當前氣溫：{temp}°C")
        print(f"💨 風速：{wind} km/h")
    else:
        print(f"連線失敗，代碼：{response.status_code}")
except Exception as e:
    print(f"錯誤：{e}")
