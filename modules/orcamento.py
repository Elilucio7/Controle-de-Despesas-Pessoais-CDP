import modules.bancodados as bancodados
import datetime
from modules.config import config

banco = bancodados.BancoDados()

class orcamento:
    def __init__(self):
        self.hoje = datetime.date.today()
        self.mes_referencia = self.hoje.strftime("%m/%Y")
        self.cfg = config()

    def calcular_orcamento(self):
        dados = self._buscar_dados_mensais()
        total_receitas = 0.0
        total_despesas = 0.0
        
        for nome, valor, categoria, data_str, descricao, forma_pagamento in dados:
            tipo_categoria = self._buscar_tipo_categoria_simples(categoria)
            if tipo_categoria == 2:
                total_receitas += valor
            elif tipo_categoria == 1:
                total_despesas += valor
        saldo_disponivel = total_receitas - total_despesas
        percentual_meta = self.cfg.meta_economia
        valor_meta_economia = total_receitas * (percentual_meta / 100)
        atingiu_meta = saldo_disponivel >= valor_meta_economia

        return {
            'total_receitas': total_receitas,
            'total_despesas': total_despesas,
            'saldo_disponivel': saldo_disponivel,
            'mes_referencia': self.mes_referencia,
            'meta_economia_valor': valor_meta_economia,
            'percentual_meta': percentual_meta,
            'atingiu_meta': atingiu_meta
        }

    def _buscar_tipo_categoria_simples(self, categoria_nome):
        banco.c.execute("SELECT tipo FROM categorias WHERE categoria = ?", (categoria_nome,))
        resultado = banco.c.fetchone()
        return int(resultado[0]) if resultado else 0

    def _buscar_dados_mensais(self):
        mes = self.hoje.month
        ano = self.hoje.year
        mes_ano_str = f"{mes:02d}/{ano}"
        query = f"SELECT nome, valor, categoria, data, descricao, forma_pagamento FROM dados WHERE data LIKE '__/{mes_ano_str}'"
        banco.c.execute(query)
        return banco.c.fetchall()