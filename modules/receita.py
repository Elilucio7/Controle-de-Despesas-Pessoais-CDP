from modules.cad_recdes import cad_recdes
import modules.bancodados as bancodados
import datetime

banco = bancodados.BancoDados()

class receita(cad_recdes):
    lista_receita = cad_recdes.listar_receitas()
    def __init__(self, nome = None, valor = None, data = None, limite = None):
        super().__init__(nome, tipo = 2, valor = valor, data = data, limite=limite)
        self.forma_pagamento = None

    def _coletar_data(self):
        while True:
            data_input = str(input())
            try:
                data = datetime.datetime.strptime(data_input, "%d/%m/%Y").date()
                return data.strftime("%d/%m/%Y")
            except ValueError:
                print("Data inválida! Digite novamente (DD/MM/AAAA): ")

    def cad_rec(self):
        print("Digite o nome da receita (Título resumido): ")
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
                if self.valor <= 0:
                    print("O valor deve ser maior que zero. Digite novamente: ")
                    continue
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
        print("Digite a descrição detalhada da receita: ")
        self.descricao = str(input())
        data_string = self.data.strftime("%d/%m/%Y")
        banco.inserir_dado(self.nome, self.valor, self.categoria, data_string, self.descricao, self.forma_pagamento)
        print("Receita cadastrada com sucesso.")

    def ver_receita(self):
        self.lista_receita = cad_recdes.listar_receitas()