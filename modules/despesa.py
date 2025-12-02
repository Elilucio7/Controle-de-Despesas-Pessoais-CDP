from modules.cad_recdes import cad_recdes
import datetime
class despesa(cad_recdes):
    lista_despesa = {k: v for k, v in cad_recdes.lista_dados.items() if v == 1}
    def __init__(self, nome = None, valor = None, data = None, limite = None):
        super().__init__(nome, tipo = 1, valor = valor, data = data, limite=limite)

    def cad_des(self):
        print("Digite o nome da despesa: ")
        while True:
            self.nome = str(input())
            if self.nome in self.lista_despesa:
                print("Despesa já cadastrada! Digite novamente: ")
            else:
                break
        print("Digite o valor da despesa: ")
        while True:
            try:
                self.valor = self.tentar_valor(input(), "1")
                if self.valor > self.limite:
                    print("Valor superior ao limite da categoria. Digite um valor novo: ")
                    self.valor = self.tentar_valor(input(), "1")
                break
            except ValueError:
                print("Valor inválido! Digite novamente: ")
        print("Digite a data da despesa (DD/MM/AAAA): ")
        while True:
            data_input = str(input())
            try:
                self.data = datetime.datetime.strptime(data_input, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data inválida! Digite novamente (DD/MM/AAAA): ")



