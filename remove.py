def remove_from_shopping_list(self, product_name):
    """Удаляет продукт из списка покупок по product_name."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")

    try:
        self.cursor.execute("DELETE FROM shopping_list WHERE product_name = ?", (product_name,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            return True, "Продукт успешно удален из списка покупок."
        else:
            return False, "Продукт с таким product_name не найден в списке покупок."
    except Exception as e:
        self.conn.rollback()
        return False, f"Ошибка удаления продукта из списка покупок: {e}"