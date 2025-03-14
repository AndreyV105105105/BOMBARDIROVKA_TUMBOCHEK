def add_product_in_bd(self, product_data):
    """Добавляет продукт в таблицу products."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")

    try:
        nutrition_info_json = json.dumps(product_data.get('nutrition_info', {}))
        added_history = json.dumps({'1': datetime.now().isoformat()})

        self.cursor.execute("""
            INSERT INTO products (product_name, product_type, manufacture_date, expiry_date, number, quantity, unit, nutrition_info, measurement_type, added_history, removed_history)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            product_data["product_name"],
            product_data["product_type"],
            product_data["manufacture_date"],
            product_data["expiry_date"],
            1,
            product_data["quantity"],
            product_data["unit"],
            nutrition_info_json,
            product_data["measurement_type"],
            added_history,
            json.dumps({})
        )
                            )

        self.conn.commit()
        return True, "Продукт успешно добавлен в холодильник."
    except Exception as e:
        self.conn.rollback()
        return False, f"Ошибка добавления продукта: {e}"