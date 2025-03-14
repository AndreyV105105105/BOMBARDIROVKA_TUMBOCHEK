def search_products(self, search_term=None, search_type=None):
    """Поиск продуктов по названию и/или типу."""
    if not self.conn or not self.cursor:
        raise Exception("Нет подключения к БД. Сначала нужно вызвать connect()")
    query = "SELECT * FROM products WHERE 1=1"
    params = []
    if search_term:
        query += " AND product_name LIKE ?"
        params.append(f"%{search_term}%")
    if search_type:
        query += " AND product_type LIKE ?"
        params.append(f"%{search_type}%")

    self.cursor.execute(query, params)
    rows = self.cursor.fetchall()
    products = []
    for row in rows:
        product = self._row_to_dict(row)
        products.append(product)

    return products