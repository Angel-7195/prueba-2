class CuentaBanco:
    def __init__(self, titular, saldo, tipo_cuenta, activa=True):
        self.titular = titular
        self.__saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.activa = activa

    def depositar(self, cantidad):
        if not self.activa:
            return "la cuenta no esta activa. No se puede depositar"
        if cantidad > 0:
            self.__saldo += cantidad
            return f"deposito exitoso. Saldo ${self.__saldo}"
        else:
            return "Cantidad invalida"

    
    def retirar(self, cantidad):
        if not self.activa:
            return "la cuenta no esta activa. No se puede retirar"
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Saldo ${self.__saldo}"
        else:
            return "Fondos insuficientes o cantidad invalida"

    def consultar_saldo(self):
        if not self.activa:
            return "La cuenta no esta activa"
        return f"Saldo actual: ${self.__saldo}"

    
    def obtener_resumen(self):
        estado = "activa" if self.activa else "inactiva"
        return(f"Titular: {self.titular}\n"
               f"Tipo de cuenta: {self.tipo_cuenta}\n"
               f"saldo: {self.__saldo}\n"
               f"estado: {estado}"

        )

        
cuenta1 = CuentaBanco("Alejandro Salgar", 5000, "corriente")
cuenta2 = CuentaBanco("María López", 2000, "ahorros")

print(cuenta1.obtener_resumen())
print(cuenta1.depositar(1500))
print(cuenta1.retirar(800))
print(cuenta1.consultar_saldo())