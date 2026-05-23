# Matriz inicial con artículos [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    ["A01", "Teclado", 3, 5],
    ["A02", "Mouse", 10, 8],
    ["A03", "Monitor", 2, 4],
    ["A04", "USB", 15, 10],
    ["A05", "Impresora", 1, 3]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Recorrer la matriz y generar lista de pedidos
def generar_pedidos(inventario):
    pedidos = []
    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)
        pedidos.append([nombre, cantidad_pedir])
    return pedidos

# Mostrar resultados
lista_pedidos = generar_pedidos(inventario)
print("Lista de pedidos:")
for pedido in lista_pedidos:
    print(f"Artículo: {pedido[0]} - Cantidad a pedir: {pedido[1]}")
