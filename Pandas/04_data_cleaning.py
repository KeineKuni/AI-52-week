import pandas as pd
import numpy as np  # 學習筆記：通常用 np.nan 來代表缺失值

# 模擬一份有問題的資料
dirty_data = {
    "產品名稱": ["益生菌", "魚油", "魚油", "葉黃素", "靈芝粉"],
    "單價": [450, 600, 600, np.nan, 800],  # 葉黃素價格缺失
    "庫存量": [20, 15, 15, 12, 5],
}
df_dirty = pd.DataFrame(dirty_data)

# --- 1. 處理重複值 ---
# 學習筆記：duplicated() 檢查重複，drop_duplicates() 刪除重複
df_clean = df_dirty.drop_duplicates()

# --- 2. 處理缺失值 ---
# 學習筆記：
# 選法 A: 直接刪除含有缺失值的整列 -> df.dropna()
# 選法 B: 填補缺失值 (例如填 0 或平均數) -> df.fillna(數值)

# 這裡我們嘗試把缺失的單價填補為該欄位的「平均值」
mean_price = df_clean["單價"].mean()
df_clean["單價"] = df_clean["單價"].fillna(mean_price)

print("--- 清理後的資料 ---")
print(df_clean)
