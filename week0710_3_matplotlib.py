import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- 1. 字體設定 (修正路徑與載入方式) ---
# 使用 r"..." 避免轉義字元錯誤，並指向正確的檔案路徑
font_path = r"C:\Windows\Fonts\msjh.ttc"
font_prop = fm.FontProperties(fname=font_path)

# --- 2. 資料處理 (保持不變) ---
df = pd.read_csv("vitatiere_sales.csv")

df["淨銷售額"] = (
    df["淨銷售額"]
    .astype(str)
    .str.replace("NT\$", "", regex=True)
    .str.replace(",", "")
    .str.strip()
)
df["淨銷售額"] = pd.to_numeric(df["淨銷售額"])
df["發佈日期"] = pd.to_datetime(df["發佈日期"])

# --- 3. 圓餅圖繪製 (修正字體套用方式) ---
product_counts = df["產品"].dropna().value_counts()

plt.figure(figsize=(10, 8))

# 使用 textprops 來傳遞字體設定給 labels
plt.pie(
    product_counts,
    labels=product_counts.index,
    autopct="%1.1f%%",
    textprops={"fontproperties": font_prop},
)

# 標題也要記得套用字體
plt.title("VitaTiere 產品銷售分佈", fontproperties=font_prop, fontsize=16)
plt.show()
