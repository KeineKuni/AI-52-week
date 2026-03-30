import numpy as np

ratings = np.array([[5, 3, 4], [2, 4, 2], [4, 5, 5]])

# 假設我們要給每一列（每個類別）分別加上不同的補償值
# 補償值：食品+1, 用品+2, 寵物保健+0
bonus = np.array([1, 2, 0])

# --- 學習筆記 ---
# 這裡 ratings 是 (3, 3)，bonus 是 (3,)
# NumPy 會自動把 bonus 「拉長」成 (3, 3) 的樣子來跟 ratings 相加
# 這就叫「廣播」
# ---
new_ratings = ratings + bonus

print("加上補償後的評分：")
print(new_ratings)
