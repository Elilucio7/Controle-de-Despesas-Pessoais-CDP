import json
import os

class config:
    def __init__(self, db_file='settings.json'):
        self.db_file = db_file
        self.padrao = {"min_alerta_gasto": 500.0, "meses_comparativo": 3, "meta_economia": 20.0}
        self.dados = self._carregar()

    def _carregar(self):
        if not os.path.exists(self.db_file):
            self._salvar(self.padrao)
            return self.padrao
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Erro ao carregar o arquivo de configuração. Usando valores padrão.")
            self._salvar(self.padrao)
            return self.padrao

    def _salvar(self, dados):
        with open(self.db_file, 'w') as f:
            json.dump(dados, f, indent=4)

    @property
    def min_alerta_gasto(self):
        return self.dados.get("min_alerta_gasto", 500.0)

    @min_alerta_gasto.setter
    def min_alerta_gasto(self, valor):
        self.dados["min_alerta_gasto"] = float(valor)
        self._salvar(self.dados)

    @property
    def meses_comparativo(self):
        return self.dados.get("meses_comparativo", 3)

    @meses_comparativo.setter
    def meses_comparativo(self, valor):
        self.dados["meses_comparativo"] = int(valor)
        self._salvar(self.dados)

    @property
    def meta_economia(self):
        return self.dados.get("meta_economia", 20.0)

    @meta_economia.setter
    def meta_economia(self, valor):
        if 0 <= float(valor) <= 100:
            self.dados["meta_economia"] = float(valor)
            self._salvar(self.dados)
        else:
            print("A meta deve ser entre 0 e 100%.")

    def menu_configuracao(self):
        while True:
            print("\n--- Configurações do Sistema ---")
            print(f"1 - Valor mínimo para alerta de gasto alto (Atual: R${self.min_alerta_gasto:.2f})")
            print(f"2 - Meses para relatório comparativo (Atual: {self.meses_comparativo})")
            print(f"3 - Meta de economia mensal % (Atual: {self.meta_economia}%)")
            print(f"4 - Voltar")
            
            op = input("Escolha uma opção: ")
            
            if op == '1':
                try:
                    val = float(input("Novo valor para alerta: "))
                    self.min_alerta_gasto = val
                except ValueError:
                    print("Valor inválido.")
            elif op == '2':
                try:
                    val = int(input("Novo número de meses: "))
                    self.meses_comparativo = val
                except ValueError:
                    print("Valor inválido.")
            elif op == '3':
                try:
                    val = float(input("Nova porcentagem de meta (0-100): "))
                    self.meta_economia = val
                except ValueError:
                    print("Valor inválido.")
            elif op == '4':
                break
            else:
                print("Opção inválida.")