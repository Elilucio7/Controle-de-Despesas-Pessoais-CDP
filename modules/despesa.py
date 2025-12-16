from modules.cad_recdes import cad_recdes
import modules.bancodados as bancodados
import datetime
from modules.alerta import alerta

banco = bancodados.BancoDados()

class despesa(cad_recdes):
    lista_despesa = cad_recdes.listar_despesas()
    def __init__(self, nome = None, valor = None, data = None, limite = None):
        super().__init__(nome, tipo = 1, valor = valor, data = data, limite=limite)
        self.alerta_sistema = alerta()

    def _coletar_forma_pagamento(self):
        formas = ["Dinheiro", "Debito", "Credito", "PIX", "Outro"]
        print("Selecione a forma de pagamento: ")
        for i, f in enumerate(formas):
            print(f"[{i+1}] {f}")
        while True:
            try:
                escolha = int(input("Selecione o número: "))
                if 1 <= escolha <= len(formas):
                    return formas[escolha-1]
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

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
                valor_temp = self.tentar_valor(input(), "1")
                if valor_temp <= 0:
                    print("O valor deve ser maior que zero.")
                    continue
                if not self.alerta_sistema.checar_gasto_elevado(valor_temp):
                    return 
                gasto_atual_categoria = banco.somar_gastos_categoria(self.categoria)
                limite_cat = banco.buscar_limite_categoria(self.categoria)
                if not self.alerta_sistema.checar_limite_categoria(gasto_atual_categoria, valor_temp, limite_cat, self.categoria):
                     return
                self.valor = valor_temp
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
        print("Digite a descrição detalhada da despesa: ")
        self.descricao = str(input())
        self.forma_pagamento = self._coletar_forma_pagamento()
        data_string = self.data.strftime("%d/%m/%Y")
        banco.inserir_dado(self.nome, self.valor, self.categoria, data_string, self.descricao, self.forma_pagamento)
        print("Despesa cadastrada com sucesso.")

    def ver_despesa(self):
        self.lista_despesa = cad_recdes.listar_despesas()
