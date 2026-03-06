import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- 1. 環境設定：中文與字體 ---
# 請確保路徑正確，若在 Mac 上則路徑會不同
font_path = r"C:\Windows\Fonts\msjh.ttc"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["axes.unicode_minus"] = False  # 讓負號能正常顯示


# --- 2. 定義自動化清洗函式 ---
def clean_order_data(file_path):
    """
    輸入 CSV 路徑，回傳清洗後且僅包含『已完成』訂單的 DataFrame
    """
    # 讀取資料
    df = pd.read_csv(file_path, encoding="utf-8-sig")

    # 過濾訂單：只保留已完成 (completed) 的交易
    # 這能確保你的營收分析不會被取消或退款的訂單干擾
    df = df[df["狀態"] == "completed"].copy()

    # 清洗金額欄位
    df["淨銷售額"] = (
        df["淨銷售額"]
        .astype(str)
        .str.replace("NT\$", "", regex=True)
        .str.replace(",", "")
        .str.strip()
    )
    df["淨銷售額"] = pd.to_numeric(df["淨銷售額"])

    # 轉換日期格式
    df["發佈日期"] = pd.to_datetime(df["發佈日期"])

    return df


# --- 3. 實際執行 ---
# 之後你只要換掉檔名，整套邏輯就能重複使用
file_name = "vitatiere_sales.csv"
clean_df = clean_order_data(file_name)

print(f"✅ 資料清洗完成！共計 {len(clean_df)} 筆有效訂單。")
print(clean_df[["發佈日期", "淨銷售額", "狀態"]].head())
