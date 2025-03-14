def update_product_quantity(self, product_name, expiry_date, status_number=True):
    """Обновляет количество продукта."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")

    try:
        current_product = self.get_product_in_bd(product_name, expiry_date)
        if not current_product:
            return False, f"Продукт с name = {product_name} и expiry_date = {expiry_date} не найден"
        self.cursor.execute("SELECT number FROM products WHERE product_name = ? AND expiry_date = ?",
                            (product_name, expiry_date,))
        now_number = int(self.cursor.fetchone()[0])
        if status_number:
            now_number += 1
        else:
            now_number -= 1
        if now_number < 0:
            now_number = 0
        n = current_product.get("added_history", "{}")
        added_history = json.loads(n)
        added_history[str(now_number)] = datetime.now().isoformat()
        added_history_json = json.dumps(added_history)
        self.cursor.execute("""
              UPDATE products
              SET number = ?,
              added_history = ?
              WHERE product_name = ? AND expiry_date = ?
            """, (now_number, added_history_json, product_name, expiry_date,))
        self.conn.commit()
        return now_number, f"Количество продукта с name = {product_name} и expiry_date = {expiry_date} обновлено"
    except Exception as e:
        self.conn.rollback()
        return False, f"Ошибка при обновлении количества продукта: {e}"