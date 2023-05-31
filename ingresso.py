class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprime_valor(self):
        print(f"o valor do ingresso foi {self.valor}")


class Vip(Ingresso):
    def __init__(self, valor, valor_adicional):
        super().__init__(valor)
        self.valor_adicional = valor_adicional

    def imprime_valor(self, valor_adicional):
        self.valor_adicional = valor_adicional
        a = (valor_adicional * self.valor) / 100
        print(f"o valor do ingresso com adicional: {self.valor + a}")


g1 = Ingresso(20)
g1.imprime_valor()
