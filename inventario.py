class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id, nombre, precio, categoria):
        self.productos.append({"id": id, "nombre": nombre, "precio": precio, "categoria": categoria})
    
    def ordenar_productos(self, clave="nombre", descendente=False):
        return sorted(self.productos, key=lambda x: x[clave], reverse=descendente)
    
    def buscar_producto_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p["nombre"].lower()]
    
    def buscar_producto_por_rango_precio(self, precio_min, precio_max):
        return [p for p in self.productos if precio_min <= p["precio"] <= precio_max]
    
    def mostrar_productos(self, productos=None):
        if productos is None:
            productos = self.productos
        for p in productos:
            print(f"ID: {p['id']}, Nombre: {p['nombre']}, Precio: {p['precio']}, Categoría: {p['categoria']}")
