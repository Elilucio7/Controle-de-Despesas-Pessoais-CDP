import modules.bancodados as bancodados
from collections import defaultdict
import datetime
from modules.orcamento import orcamento
from modules.config import config
from modules.alerta import alerta

banco = bancodados.BancoDados()

class relatorio:
    def __init__(self):
        self.orcamento_calc = orcamento()
        self.cfg = config()
        self.alerta_sistema = alerta()
    
    def _exibir_orcamento_mensal(self):
        orc_dados = self.orcamento_calc.calcular_orcamento()
        print(f"\n--- Orçamento Mensal - {orc_dados['mes_referencia']} ---")
        print(f"Total de Receitas: R${orc_dados['total_receitas']:.2f}")
        print(f"Total de Despesas: R${orc_dados['total_despesas']:.2f}")
        print(f"SALDO DISPONÍVEL:  R${orc_dados['saldo_disponivel']:.2f}")
        self.alerta_sistema.checar_deficit_orcamentario(orc_dados['saldo_disponivel'])
        status_meta = "Meta atingida" if orc_dados['atingiu_meta'] else "Meta não atingida"
        print(f"\n--- Meta de Economia ({orc_dados['percentual_meta']}%) ---")
        print(f"Meta a economizar: R${orc_dados['meta_economia_valor']:.2f}")
        print(f"Status: {status_meta}")

    def gerar_relatorios(self):
        print("\n--- Relatórios e Estatísticas ---")
        despesas_totais = self._buscar_todas_despesas()
        if not despesas_totais:
            print("Nenhuma despesa registrada para gerar relatórios.")
            return
        total_geral_despesas = sum(dado[1] for dado in despesas_totais)
        self._total_por_categoria(despesas_totais, total_geral_despesas)
        self._grupos_por_forma_pagamento(despesas_totais)
        self._mes_mais_economico(despesas_totais)
        self._comparativo_ultimos_meses()
        self._exibir_orcamento_mensal()
        
    def _buscar_todas_despesas(self):
        banco.c.execute("SELECT nome, valor, categoria, data, descricao, forma_pagamento FROM dados")
        todos_dados = banco.c.fetchall()
        todas_despesas = []
        for nome, valor, categoria, data, descricao, forma_pagamento in todos_dados:
            tipo = self._buscar_tipo_categoria_simples(categoria) 
            if tipo == 1:
                todas_despesas.append((nome, valor, categoria, data, descricao, forma_pagamento))
        return todas_despesas

    def _total_por_categoria(self, despesas_totais, total_geral_despesas):
        gastos_por_categoria = defaultdict(float)
        for nome, valor, categoria, data, descricao, forma_pagamento in despesas_totais:
            gastos_por_categoria[categoria] += valor
        print("\n--- Total de Despesas por Categoria ---")
        for categoria, total in gastos_por_categoria.items():
            percentual = (total / total_geral_despesas) * 100
            print(f"Categoria: {categoria} | Total: R${total:.2f} ({percentual:.2f}%)")

    def _grupos_por_forma_pagamento(self, despesas_totais):
        gastos_por_forma = defaultdict(float)
        for nome, valor, categoria, data, descricao, forma_pagamento in despesas_totais:
            gastos_por_forma[forma_pagamento] += valor
        total_geral_despesas = sum(gastos_por_forma.values())
        print("\n--- Total de Despesas por Forma de Pagamento ---")
        for forma, total in gastos_por_forma.items():
            percentual = (total / total_geral_despesas) * 100
            print(f"Forma: {forma} | Total: R${total:.2f} ({percentual:.2f}%)")
            
    def _mes_mais_economico(self, despesas_totais):
        gastos_por_mes = defaultdict(float)
        for nome, valor, categoria, data_str, descricao, forma_pagamento in despesas_totais:
            try:
                data = datetime.datetime.strptime(data_str, "%d/%m/%Y")
                mes_ano = data.strftime("%m/%Y")
                gastos_por_mes[mes_ano] += valor
            except ValueError:
                pass 
        if not gastos_por_mes:
            print("\nNão há dados suficientes para determinar o mês mais econômico.")
            return
        mes_economico = min(gastos_por_mes, key=gastos_por_mes.get)
        menor_gasto = gastos_por_mes[mes_economico]
        print(f"\n--- Estatísticas Mensais ---")
        print(f"Mês mais econômico (Menor Despesa Total): {mes_economico} com R${menor_gasto:.2f}")

    def _comparativo_ultimos_meses(self):
        hoje = datetime.date.today()
        comparativo = defaultdict(lambda: {'Receita': 0.0, 'Despesa': 0.0})
        qtd_meses = self.cfg.meses_comparativo
        print(f"\n--- Comparativo Receitas e Despesas (Últimos {qtd_meses} Meses) ---")
        for i in range(qtd_meses):
            mes = hoje.month - i
            ano = hoje.year
            while mes <= 0:
                mes += 12
                ano -= 1
            mes_ano_str = f"{mes:02d}/{ano}"
            query = f"SELECT valor, categoria, data FROM dados WHERE data LIKE '__/{mes_ano_str}'"
            banco.c.execute(query)
            dados_mes = banco.c.fetchall()
            for valor, categoria, data in dados_mes:
                tipo = self._buscar_tipo_categoria_simples(categoria)
                if tipo == 1:
                    comparativo[mes_ano_str]['Despesa'] += valor
                elif tipo == 2:
                    comparativo[mes_ano_str]['Receita'] += valor
        
        for mes_ano, totais in sorted(comparativo.items(), key=lambda item: datetime.datetime.strptime(item[0], "%m/%Y")):
            print(f"\n{mes_ano}:")
            print(f"  Receitas: R${totais['Receita']:.2f}")
            print(f"  Despesas: R${totais['Despesa']:.2f}")
            print(f"  SALDO: R${totais['Receita'] - totais['Despesa']:.2f}")

    def _buscar_tipo_categoria_simples(self, categoria_nome):
        banco.c.execute("SELECT tipo FROM categorias WHERE categoria = ?", (categoria_nome,))
        resultado = banco.c.fetchone()
        return int(resultado[0]) if resultado else 0

        