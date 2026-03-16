import requests


class WeatherTool:
    def __init__(self, lat, lon):
        self.url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    def get_temp(self):
        # 回傳溫度
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data["current_weather"]["temperature"]
        return None


# 使用方式
taipei_weather = WeatherTool(25.0478, 121.5319)
print(f"目前溫度是：{taipei_weather.get_temp()}")
