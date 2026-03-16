import psycopg

# 1. 建立與 PostgreSQL 的連線
conn = psycopg.connect("dbname=vitatiere user=kuni password=yourpassword host=localhost")

# 2. 開啟游標
cur = conn.cursor()

# 3. 執行建立資料表的 SQL
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER,
        description TEXT
    );
""")

# 4. 提交並關閉
conn.commit()
cur.close()
conn.close()