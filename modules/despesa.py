from modules.cad_recdes import cad_recdes
import modules.bancodados as bancodados
import datetime

banco = bancodados.BancoDados()

class despesa(cad_recdes):
    lista_despesa = cad_recdes.listar_despesas()
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
                if self.limite is not None and self.valor > self.limite:
                    print("Valor superior ao limite da categoria. Digite um valor novo: ")
                else:
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
        data_string = self.data.strftime("%d/%m/%Y")
        banco.inserir_dado(self.nome, self.valor, self.categoria, data_string)



