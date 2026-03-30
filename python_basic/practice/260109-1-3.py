# 產品編號作為 key，裡面包著產品資訊
vita_products = {
    "A01": {"name": "骨關節粉包", "stock": 15},
    "B02": {"name": "皮毛保健粉包", "stock": 5},
    "C03": {"name": "腸胃益生菌粉包", "stock": 1}
}

threshold = 10

for sku,product in vita_products.items():
    if product["stock"]<threshold:
        print(f"庫存不足的產品:{product["name"]}")