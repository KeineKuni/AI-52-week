import pandas as pd
import io
import re


def clean_order_data_v2(file_path):
    # --- 步驟 1: 預處理原始文字 ---
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # 使用 Regex 尋找 NT$ 後面接數字與逗號的組合，並移除逗號
    # 例如把 "NT$1,200" 變成 "NT$1200"
    content = re.sub(r"(NT\$\d+),(\d+)", r"\1\2", content)

    # --- 步驟 2: 將處理過的文字轉為 DataFrame ---
    df = pd.read_csv(io.StringIO(content))

    # --- 步驟 3: 過濾與格式轉換 ---
    # 只保留已完成訂單
    df_cleaned = df[df["狀態"] == "completed"].copy()

    # 清洗金額 (現在沒有逗號了，處理更簡單)
    df_cleaned["淨銷售額"] = (
        df_cleaned["淨銷售額"]
        .astype(str)
        .str.replace("NT\$", "", regex=True)
        .str.strip()
    )
    df_cleaned["淨銷售額"] = pd.to_numeric(df_cleaned["淨銷售額"])

    # 轉換日期
    df_cleaned["發佈日期"] = pd.to_datetime(df_cleaned["發佈日期"])

    return df_cleaned


# --- 實作演練：重新測試 ---
csv_content = """訂單號碼,發佈日期,狀態,淨銷售額,產品
1001,2026-03-01 10:30,completed,"NT$1,200",犬貓益生菌
1002,2026-03-01 11:15,cancelled,NT$550,貓用零食
1003,2026-03-02 14:00,completed,"NT$2,150",關節保健組
1004,2026-03-02 15:20,refunded,NT$800,犬用維他命
"""

with open("test_sales_v2.csv", "w", encoding="utf-8-sig") as f:
    f.write(csv_content)

result_df = clean_order_data_v2("test_sales_v2.csv")

# 假設 result_df 是我們清洗後的資料
total_revenue = result_df["淨銷售額"].sum()
order_count = len(result_df)
avg_order_value = total_revenue / order_count if order_count > 0 else 0

print(f"===== VitaTiere 月營運摘要 =====")
print(f"💰 總銷售額：NT$ {total_revenue:,.0f}")
print(f"📦 總訂單數：{order_count} 筆")
print(f"💎 平均客單價：NT$ {avg_order_value:,.0f}")
print(f"================================")
