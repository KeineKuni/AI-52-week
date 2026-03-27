# put:更新現有產品
from pydantic import BaseModel


# 1. 定義產品的資料結構（確保進來的資料格式正確）
class Product(BaseModel):
    id: int
    name: str
    brand: str
    price: int


# 2. 用 PUT 修正產品
@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    # 檢查該產品是否存在
    if product_id not in products:
        return {"error": "找不到該產品，無法更新"}

    # 更新資料
    products[product_id] = product.dict()
    return {
        "message": f"產品 {product_id} 已成功更新",
        "updated_data": products[product_id],
    }
