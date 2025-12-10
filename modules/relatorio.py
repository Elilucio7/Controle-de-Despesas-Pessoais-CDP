import modules.bancodados as bancodados
from collections import defaultdict
import datetime

banco = bancodados.BancoDados()

class relatorio:
    def __init__(self):
        pass

    def gerar_relatorios(self):
        print("\n--- Relatórios e Estatísticas ---")
        
        despesas_totais = self._buscar_todas_despesas()
        
        if not despesas_totais:
            print("Nenhuma despesa registrada para gerar relatórios.")
            return

        total_geral_despesas = sum(dado[1] for dado in despesas_totais)

        self._total_por_categoria(despesas_totais, total_geral_despesas)
        
        self._mes_mais_economico(despesas_totais)
        
        self._comparativo_ultimos_meses()
        
    def _buscar_todas_despesas(self):
        banco.c.execute("SELECT nome, valor, categoria, data FROM dados")
        todos_dados = banco.c.fetchall()
        
        todas_despesas = []
        for nome, valor, categoria, data in todos_dados:
            tipo = self._buscar_tipo_categoria_simples(categoria) 
            if tipo == 1:
                todas_despesas.append((nome, valor, categoria, data))
        return todas_despesas

    def _total_por_categoria(self, despesas_totais, total_geral_despesas):
        despesas_por_categoria = defaultdict(float)
        
        for nome, valor, categoria, data in despesas_totais:
            despesas_por_categoria[categoria] += valor
            
        print("\n--- Total e Percentual de Despesas por Categoria ---")
        for categoria, total in despesas_por_categoria.items():
            percentual = (total / total_geral_despesas) * 100
            print(f"  {categoria}: R${total:.2f} ({percentual:.2f}%)")

    def _mes_mais_economico(self, despesas_totais):
        despesas_por_mes = defaultdict(float)
        
        for nome, valor, categoria, data_str in despesas_totais:
            mes_ano = data_str[3:] 
            despesas_por_mes[mes_ano] += valor
            
        if not despesas_por_mes:
            return
            
        mes_economico = min(despesas_por_mes, key=despesas_por_mes.get)
        valor_economico = despesas_por_mes[mes_economico]
        
        print(f"\n--- Mês Mais Econômico ---")
        print(f"O mês mais econômico foi {mes_economico} com total de despesas de R${valor_economico:.2f}.")

    def _comparativo_ultimos_meses(self):
        hoje = datetime.date.today()
        comparativo = defaultdict(lambda: {'Receita': 0.0, 'Despesa': 0.0})

        print(f"\n--- Comparativo Receitas e Despesas (Últimos 3 Meses) ---")

        for i in range(3):
            mes = hoje.month - i
            ano = hoje.year
            if mes <= 0:
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