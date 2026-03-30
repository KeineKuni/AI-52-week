def process_input(data):
    result = None
    try:
        # A. 可能發生 ValueError (轉換失敗)
        number = int(data)
    except ValueError:
        # B. 發生轉換錯誤時執行
        print(f"🚨 輸入資料 '{data}' 無法轉換為數字。")
    else:
        # C. 只有當 try 區塊成功 (沒有發生錯誤) 時才執行
        print("✅ 轉換成功，正在進行數學運算...")
        result = number * 2
    finally:
        # D. 無論有無錯誤，最後都會執行
        print("--- 輸入處理流程結束 ---")
        return result

# 測試成功案例 (執行 A -> C -> D)
print("結果 (Success):", process_input("10")) 
print("-" * 20)

# 測試失敗案例 (執行 A -> B -> D)
print("結果 (Failure):", process_input("abc"))