class Ticket:
    def __init__(self, codigo, patente, tipo, pago, pais, km):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.pago = pago
        self.pais = pais
        self.km = km

    def __str__(self):
        paises = ("Argentina", "Chile", "Brasil", "Bolivia", "Paraguay", "Uruguay", "Otro")
        vehiculos = ("motocicleta", "automóvil", "camión")
        pago = ("manual", "telepeaje")
        return f"Código: {self.codigo}, Patente: {self.patente}, Tipo de vehículo: {vehiculos[int(self.tipo)]}, " \
               f"Forma de pago: {pago[int(self.pago)-1]}, País de cabina: {paises[int(self.pais)]}, Km recorridos: {self.km}"
