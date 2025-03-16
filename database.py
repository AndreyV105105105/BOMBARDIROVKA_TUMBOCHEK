import sqlite3
import json
from datetime import datetime, timedelta
import uuid


class DatabaseManager:
    def __init__(self, db_name="smart_fridge.db"):
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
            CREATE TABLE IF NOT EXISTS pazles (
                href INTEGER PRIMARY KEY AUTOINCREMENT,
                full TEXT NOT NULL,
                modul TEXT NOT NULL,
                base TEXT NOT NULL,
                base_rad TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_product_in_bd(self, product_data):
        if not self.conn or not self.cursor:
            raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")

        try:
            self.cursor.execute("""
                INSERT INTO products (href, full, modul, base, base_rad)
                VALUES (?, ?, ?, ?, ?)
            """, (
                product_data['href'],
                product_data['full'],
                product_data['modul'],
                product_data['base'],
                product_data['base_rad']
            )
                                )

            self.conn.commit()
            return True, "Продукт успешно добавлен в БД>."
        except Exception as e:
            self.conn.rollback()
            return False, f"Ошибка добавления продукта: {e}"


    def get_product_by_id(self, product_id):
        """Получает продукт из таблицы products по ID."""
        if not self.conn or not self.cursor:
            raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")
        self.cursor.execute("SELECT * FROM products WHERE href = ?", (product_id,))
        row = self.cursor.fetchone()
        if row:
            return self._row_to_dict(row)
        else:
            return None


    # def get_all_products(self):
    #     """Получает все продукты из таблицы products."""
    #     if not self.conn or not self.cursor:
    #         raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")
    #
    #     self.cursor.execute("SELECT * FROM products")
    #     rows = self.cursor.fetchall()
    #     products = []
    #     for row in rows:
    #         if row[5] > 0:
    #             product = self._row_to_dict(row)
    #             products.append(product)
    #     return products



    def _row_to_dict(self, row):
        """Преобразует строку из БД в словарь."""
        nutrition_info = row[8]
        return {
            "id": row[0],
            "product_name": row[1],
            "product_type": row[2],
            "manufacture_date": row[3],
            "expiry_date": row[4],
            "number": row[5],
            "quantity": row[6],
            "unit": row[7],
            "nutrition_info": json.loads(nutrition_info) if nutrition_info else None,
            "measurement_type": row[9],
            "added_history": row[10] if row[10] else None,
            "removed_history": row[11] if row[11] else None
        }


    def _shopping_row_to_dict(self, row):
        return {
            "id": row[0],
            "product_name": row[1],
            "quantity": row[2],
            "added_at": row[3]
        }


