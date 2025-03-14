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