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
                href INTEGER PRIMARY KEY AUTOINCREMENT,
                full TEXT NOT NULL,
                modul TEXT NOT NULL,
                base DATE NOT NULL,
                base_rad DATE NOT NULL
            )
        """)
        self.conn.commit()
