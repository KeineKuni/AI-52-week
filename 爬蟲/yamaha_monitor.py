import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# --- 學習筆記：配置區 ---
DB_FILE = "yamaha_history.csv"
TARGET_URL = "https://www.yamaha-motor.com.tw/news/news"
MAX_PAGES = 30  # 業界習慣：設定抓取上限，避免無窮迴圈或被封鎖


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def scrape_all_pages():
    """負責『自動翻頁』抓取的邏輯"""
    driver = get_driver()
    all_events = []

    try:
        driver.get(TARGET_URL)
        time.sleep(3)

        for page in range(1, MAX_PAGES + 1):
            print(f"📄 正在處理第 {page} 頁...")

            # 解析當前頁面內容
            soup = BeautifulSoup(driver.page_source, "html.parser")
            items = soup.find_all("a", class_="card--news--xl")

            for item in items:
                title = item.find("h2", class_="title").text.strip()
                date_tag = item.find("div", class_="date")
                date = date_tag.text.strip() if date_tag else "最新消息"
                all_events.append({"日期": date, "標題": title})

            # --- 學習筆記：尋找並點擊『下一頁』 ---
            if page < MAX_PAGES:
                try:
                    # 尋找頁碼按鈕 (這部分需要根據 HTML 精準定位)
                    next_page_num = page + 1
                    next_btn = driver.find_element(
                        By.CSS_SELECTOR, f"a.pager_link[data-page='{next_page_num}']"
                    )
                    driver.execute_script(
                        "arguments[0].click();", next_btn
                    )  # 業界常用：用 JS 點擊較穩定
                    time.sleep(2)  # 等待翻頁載入
                except Exception as e:
                    print(f"🛑 無法翻到下一頁 (可能已達末頁): {e}")
                    break
    finally:
        driver.quit()

    return pd.DataFrame(all_events)


def run_monitor():
    """主控邏輯"""
    new_df = scrape_all_pages()

    if new_df.empty:
        print("⚠️ 抓取失敗。")
        return

    # 讀取與異常處理
    try:
        old_df = (
            pd.read_csv(DB_FILE)
            if os.path.exists(DB_FILE)
            else pd.DataFrame(columns=["日期", "標題"])
        )
    except:
        old_df = pd.DataFrame(columns=["日期", "標題"])

    # 篩選出新活動 (排除已存在的標題)
    new_activities = new_df[~new_df["標題"].isin(old_df["標題"])]

    if not new_activities.empty:
        print(f"🎉 成功！發現 {len(new_activities)} 筆新資料。")
        # 合併並存檔
        updated_df = pd.concat([old_df, new_activities], ignore_index=True)
        updated_df.to_csv(DB_FILE, index=False, encoding="utf-8-sig")
    else:
        print("😴 暫無更新。")


if __name__ == "__main__":
    run_monitor()
