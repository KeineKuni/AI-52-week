# get:讀取產品資訊
from fastapi import FastAPI

# 1. 建立一個 FastAPI 應用程式實例
app = FastAPI()

# 2. 定義一個資料來源（模擬資料庫）
products = {
    123: {"name": "腸胃益生菌", "brand": "VitaTiere", "price": 630},
    456: {"name": "鴉氣管凍乾", "brand": "VitaTiere", "price": 199},
}


# 3. 設定路徑與動作
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    # 這裡會根據 product_id 回傳資料
    return products.get(product_id, {"error": "找不到該產品"})
