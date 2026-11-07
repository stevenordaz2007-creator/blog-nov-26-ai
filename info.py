"""
Arepas El Sabor - Puerto La Cruz, Venezuela
Sitio web estático para venta de arepas (Fase 1)

Este archivo es solo de referencia/documentación.
El sitio es estático (HTML/CSS/JS) y no requiere backend de Python.
"""

NOMBRE_NEGOCIO = "Arepas El Sabor"
CIUDAD = "Puerto La Cruz, Anzoátegui, Venezuela"
METODO_PAGO = "Pago Móvil y Transferencia Bancaria"
DELIVERY = True
FASE = 1

if __name__ == "__main__":
    print(f"{NOMBRE_NEGOCIO} - {CIUDAD}")
    print(f"Metodo de pago: {METODO_PAGO}")
    print(f"Delivery a domicilio: {'Si' if DELIVERY else 'No'}")
    print(f"Fase: {FASE}")
    print("Sitio estatico: index.html")