# post:新增全新產品

from pydantic import BaseModel


# 1. 定義產品的資料結構（確保進來的資料格式正確）
class Product(BaseModel):
    id: int
    name: str
    brand: str
    price: int


# 2. 建立 POST 接口來新增產品
@app.post("/products")
async def create_product(product: Product):
    # 將新產品加入到我們的 products 字典中
    products[product.id] = product.dict()
    return {"message": "產品新增成功", "data": product}
