try:
    s=int("hello")
except ValueError as e:
    print(f"錯誤類別:{e}")
    s=""