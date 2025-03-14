def get_all_products(self):
    """Получает все продукты из таблицы products."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")

    self.cursor.execute("SELECT * FROM products")
    rows = self.cursor.fetchall()
    products = []
    for row in rows:
        if row[5] > 0:
            product = self._row_to_dict(row)
            products.append(product)
    return products


def get_product_by_id(self, product_id):
    """Получает продукт из таблицы products по ID."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")
    self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = self.cursor.fetchone()
    if row:
        return self._row_to_dict(row)
    else:
        return None


def get_product_in_bd(self, product_name, expiry_date):
    """Получает продукт из таблицы products по ID."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")
    self.cursor.execute("SELECT * FROM products WHERE product_name = ? AND expiry_date = ?",
                        (product_name, expiry_date,))
    row = self.cursor.fetchone()
    if row:
        return self._row_to_dict(row)
    else:
        return None
