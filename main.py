class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        colores_permitidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in colores_permitidos:
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "electrico":
            self.tipo = tipo


class Auto:
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor: Motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        return sum(isinstance(asiento, Asiento) for asiento in self.asientos)
    
    def verificarIntegridad(self):
        registros = set()
        registros.add(self.registro)
        registros.add(self.motor.registro)
        for asiento in self.asientos:
            registros.add(asiento.registro)
        if len(registros) == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"