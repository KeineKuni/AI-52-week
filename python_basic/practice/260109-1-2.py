# 這是字典清單，更接近實際資料庫的樣子
products = [
    {"name": "骨關節粉包", "stock": 15},
    {"name": "皮毛保健粉包", "stock": 8},
    {"name": "腸胃益生菌粉包", "stock": 20}
]

# 提示：用 for p in products: 拿到的 p 會是一個小字典
# 你可以用 p["name"] 和 p["stock"] 來取值

threshold=10

for p in products:
    if p["stock"]<threshold:
        print(f"{p["name"]}庫存不足!")