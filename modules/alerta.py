from modules.config import config

class alerta:
    def __init__(self):
        self.cfg = config()

    def _confirmar_acao(self):
        confirmacao = input("Deseja prosseguir com o lançamento? (S/N): ").upper()
        return confirmacao == 'S'

    def checar_gasto_elevado(self, valor):
        limite_aviso = self.cfg.min_alerta_gasto
        if valor >= limite_aviso:
            print(f"\n---ALERTA DE ALTO VALOR---")
            print(f"O valor R${valor:.2f} excede o limite de R${limite_aviso:.2f}.")
            open("logs.txt", "a+", encoding="utf-8").write(f"ALERTA: Gasto elevado de R${valor:.2f} registrado.\n")
            return self._confirmar_acao()
        return True

    def checar_limite_categoria(self, gasto_atual, novo_valor, limite_categoria, nome_categoria):
        if limite_categoria is None or limite_categoria == 0:
            return True
        total_previsto = gasto_atual + novo_valor
        if total_previsto > limite_categoria:
            excesso = total_previsto - limite_categoria
            print(f"\n---ALERTA: LIMITE EXCEDIDO---")
            print(f"Categoria: {nome_categoria}")
            print(f"Gasto Atual: R${gasto_atual:.2f} | Novo Gasto: R${novo_valor:.2f}")
            print(f"Total Previsto: R${total_previsto:.2f} > Limite: R${limite_categoria:.2f}")
            print(f"Esta operação excederá o orçamento da categoria em R${excesso:.2f}.")
            with open("logs.txt", "a+", encoding="utf-8") as f:
                f.write(f"ALERTA: Limite de categoria '{nome_categoria}' excedido. Gasto Atual: R${gasto_atual:.2f}, Novo Gasto: R${novo_valor:.2f}, Limite: R${limite_categoria:.2f}\n")
            return self._confirmar_acao()
        return True

    def checar_deficit_orcamentario(self, saldo):
        if saldo < 0:
            print(f"\n---ALERTA: DÉFICIT ORÇAMENTÁRIO---")
            print(f"O seu saldo mensal está negativo em R${saldo:.2f}. Atenção às suas finanças!")
            open("logs.txt", "a+", encoding="utf-8").write(f"ALERTA: Déficit orçamentário de R${saldo:.2f} registrado.\n")
        else:
            print(f"\nSituação Orçamentária: Saldo positivo.")