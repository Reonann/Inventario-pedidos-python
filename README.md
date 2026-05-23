# Inventario-pedidos-python

##  Descripción
Este proyecto corresponde a la **Fase 5 – Evaluación Final POA** del curso *Fundamentos de Programación* en la UNAD.  
El programa permite auditar un inventario y determinar qué artículos necesitan ser reabastecidos, calculando la cantidad exacta a pedir según el stock actual y el stock mínimo requerido.

##  Funcionalidad
- **Entrada:** matriz con artículos en el formato `[Código, Nombre, Stock Actual, Stock Mínimo]`.
- **Proceso:** se compara el stock actual con el mínimo requerido y se calcula la diferencia.
- **Salida:** lista con el nombre del artículo y la cantidad exacta a pedir.

##  Ejemplo de uso
Matriz inicial:
```python 
inventario = [
    ["A01", "Teclado", 3, 5],
    ["A02", "Mouse", 10, 8],
    ["A03", "Monitor", 2, 4],
    ["A04", "USB", 15, 10],
    ["A05", "Impresora", 1, 3]
]
## Resultado esperado:
Lista de pedidos:
Artículo: Teclado - Cantidad a pedir: 2
Artículo: Mouse - Cantidad a pedir: 0
Artículo: Monitor - Cantidad a pedir: 2
Artículo: USB - Cantidad a pedir: 0
Artículo: Impresora - Cantidad a pedir: 2

## Autor
Diego Alejandro Salazar Rodríguez  
Universidad Nacional Abierta y a Distancia – UNAD
Curso: Fundamentos de Programación (Código 213022)
