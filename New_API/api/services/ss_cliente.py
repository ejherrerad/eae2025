from api.models.db import connection_db

def get_clientes():
    """Get all clients with their sales information"""
    with connection_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT c.id, v.fecha_venta, v.total "
                           "FROM clientes AS c "
                           "INNER JOIN ventas v ON c.id = v.cliente_id;")
            clientes = cursor.fetchall()
    return [
        {"id_cliente": c[0], "fecha_venta": c[1], "total_venta": c[2]} for c in clientes
    ]
