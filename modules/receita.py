from modules.cad_recdes import cad_recdes
import modules.bancodados as bancodados
import datetime

banco = bancodados.BancoDados()

class receita(cad_recdes):
    lista_receita = cad_recdes.listar_receitas()
    def __init__(self, nome = None, valor = None, data = None, limite = None):
        super().__init__(nome, tipo = 1, valor = valor, data = data, limite=limite)

    def cad_rec(self):
        print("Digite o nome da receita: ")
        while True:
            self.nome = str(input())
            if self.nome in self.lista_receita:
                print("Receita já cadastrada! Digite novamente: ")
            else:
                break
        print("Digite o valor da receita: ")
        while True:
            try:
                self.valor = self.tentar_valor(input(), "1")
                break
            except ValueError:
                print("Valor inválido! Digite novamente: ")
        print("Digite a data da receita (DD/MM/AAAA): ")
        while True:
            data_input = str(input())
            try:
                self.data = datetime.datetime.strptime(data_input, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data inválida! Digite novamente (DD/MM/AAAA): ")
        data_string = self.data.strftime("%d/%m/%Y")
        banco.inserir_dado(self.nome, self.valor, self.categoria, data_string)
