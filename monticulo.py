class Llamada:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad

class Nodo:
    def __init__(self, llamada):
        self.llamada = llamada
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.prioridad = [None] * 5

    def agregar_llamada(self, llamada):
        if self.prioridad[llamada.gravedad - 1] is None:
            self.prioridad[llamada.gravedad - 1] = Nodo(llamada)
        else:
            current = self.prioridad[llamada.gravedad - 1]
            prev = None
            while current is not None and current.llamada.edad <= llamada.edad:
                prev = current
                current = current.siguiente
            if prev is None:
                temp = self.prioridad[llamada.gravedad - 1]
                self.prioridad[llamada.gravedad - 1] = Nodo(llamada)
                self.prioridad[llamada.gravedad - 1].siguiente = temp
            else:
                prev.siguiente = Nodo(llamada)
                prev.siguiente.siguiente = current

    def siguiente_solicitud(self):
        for nivel in reversed(self.prioridad):
            if nivel is not None:
                llamada = nivel
                nivel = nivel.siguiente
                return llamada.llamada
        return None

    def mostrar_cola(self):
        print("Cola de prioridad para atención:")
        for nivel in self.prioridad:
            current = nivel
            while current is not None:
                print(f"Nombre: {current.llamada.nombre}, Gravedad: {current.llamada.gravedad}")
                current = current.siguiente

sistema = ColaPrioridad()

while True:
    print("\nMenú:")
    print("1. Ingresar Llamada")
    print("2. Pasar siguiente solicitud")
    print("3. Mostrar cola")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        nombre = input("Ingrese nombre completo: ")
        edad = int(input("Ingrese edad: "))
        direccion = input("Ingrese dirección: ")
        motivo = input("Ingrese motivo de la llamada: ")
        gravedad = int(input("Ingrese gravedad (1-5): "))
        llamada = Llamada(nombre, edad, direccion, motivo, gravedad)
        sistema.agregar_llamada(llamada)
        print(f"{nombre} ha sido agregado a la cola de prioridad.")

    elif opcion == "2":
        siguiente = sistema.siguiente_solicitud()
        if siguiente:
            print("Siguiente solicitud a atender:")
            print("Nombre:", siguiente.nombre)
            print("Edad:", siguiente.edad)
            print("Dirección:", siguiente.direccion)    
            print("Motivo:", siguiente.motivo)
            print("Gravedad:", siguiente.gravedad)
        else:
            print("No hay solicitudes pendientes.")

    elif opcion == "3":
        sistema.mostrar_cola()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
