import sqlite3


class DatabaseManager:
    def __init__(self, db_name="name.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Устанавливает соединение с БД."""
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def close(self):
        """Закрывает соединение с БД."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def create_tables(self):
        """Создаёт таблицы, если их нет."""
        if not self.conn or not self.cursor:
            raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                product_type TEXT NOT NULL,
                manufacture_date DATE NOT NULL,
                expiry_date DATE NOT NULL,
                number REAL NOT NULL,
                quantity REAL NOT NULL,
                unit TEXT NOT NULL,
                nutrition_info TEXT,
                measurement_type TEXT NOT NULL,
                added_history TEXT,
                removed_history TEXT
            )
        """)
        self.cursor.execute("""
          CREATE TABLE IF NOT EXISTS shopping_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            added_at DATETIME DEFAULT CURRENT_TIMESTAMP
           )
       """)
        self.conn.commit()
