import sqlite3

# データベースとテーブルの初期化関数
def init_db():
    # SQLiteデータベースに接続（ファイルがなければ自動作成）
    conn = sqlite3.connect("inquiries.db")
    cursor = conn.cursor()
    
    # 問い合わせ内容を保存するテーブルを作成（存在しない場合のみ）
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 自動採番ID
            name TEXT,                              -- ユーザー名
            email TEXT,                             -- メールアドレス
            message TEXT,                           -- 問い合わせ内容
            response TEXT,                          -- AIの応答
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 作成日時
        )
    """)
    
    # 変更を保存して接続を終了
    conn.commit()
    conn.close()

# 問い合わせデータをDBに保存する関数
def save_to_db(name, email, message, response):
    # データベースに接続
    conn = sqlite3.connect("inquiries.db")
    cursor = conn.cursor()
    
    # contactテーブルにデータを挿入
    cursor.execute("""
        INSERT INTO contact (name, email, message, response)
        VALUES (?, ?, ?, ?)
    """, (name, email, message, response))
    
    # 変更を保存して接続を終了
    conn.commit()
    conn.close()
