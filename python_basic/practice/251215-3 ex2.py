product_code = "VT-987"

# 1. 檢查是否以 "VT-" 開頭
is_vt_product = product_code.startswith("VT-")

# 2. 檢查數字部分是否為純數字
is_numeric = product_code[3:].isdigit()

# 預計輸出結果應該都是 True
print(f"VT 產品編號開頭檢查: {is_vt_product}")
print(f"數字部分純數字檢查: {is_numeric}")