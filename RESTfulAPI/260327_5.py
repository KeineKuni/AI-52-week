import requests


def check_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    response = requests.get(url)

    # 檢查狀態碼
    if response.status_code == 200:
        data = response.json()
        print(f"成功抓取！任務名稱是：{data['title']}")
    elif response.status_code == 404:
        print("哎呀，找不到這個編號的任務內容。")
    else:
        print(f"發生錯誤，狀態碼：{response.status_code}")


# 測試看看
check_todo(1)  # 應該會成功
check_todo(9999)  # 應該會顯示找不到

search_params = {"category": "supplement", "min_stock": 10}
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos", params=search_params
)
