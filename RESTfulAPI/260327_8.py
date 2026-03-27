import requests
from requests.exceptions import HTTPError


def safe_get_data(url):
    try:
        response = requests.get(url)
        # 如果狀態碼是 4xx 或 5xx，這行會觸發錯誤進入 except 區塊
        response.raise_for_status()

        return response.json()

    except HTTPError as http_err:
        if response.status_code == 500:
            print("❌ 伺服器目前大塞車或維修中，請稍後再試。")
        elif response.status_code == 404:
            print("❌ 找不到這個頁面，請檢查網址。")
    except Exception as err:
        print(f"❌ 發生了其他錯誤: {err}")


# 假設這是 VitaTiere 的 API 測試
data = safe_get_data("https://jsonplaceholder.typicode.com/posts/1")
