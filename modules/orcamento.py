import modules.bancodados as bancodados
import datetime

banco = bancodados.BancoDados()

class orcamento:
    def __init__(self):
        self.hoje = datetime.date.today()
        self.mes_referencia = self.hoje.strftime("%m/%Y")

    def calcular_e_exibir_orcamento(self):
        print(f"\n--- Orçamento Mensal - {self.mes_referencia} ---")
        
        dados = self._buscar_dados_mensais()
        
        total_receitas = 0.0
        total_despesas = 0.0
        
        for nome, valor, categoria, data_str in dados:
            tipo_categoria = self._buscar_tipo_categoria_simples(categoria)

            if tipo_categoria == 2:
                total_receitas += valor
            elif tipo_categoria == 1:
                total_despesas += valor

        saldo_disponivel = total_receitas - total_despesas

        print(f"Total de Receitas no mês: R${total_receitas:.2f}")
        print(f"Total de Despesas no mês: R${total_despesas:.2f}")
        print(f"SALDO DISPONÍVEL: R${saldo_disponivel:.2f}")

        if saldo_disponivel < 0:
            print("\n🚨 ALERTA: O saldo mensal está negativo!")

    def _buscar_tipo_categoria_simples(self, categoria_nome):
        banco.c.execute("SELECT tipo FROM categorias WHERE categoria = ?", (categoria_nome,))
        resultado = banco.c.fetchone()
        return int(resultado[0]) if resultado else 0

    def _buscar_dados_mensais(self):
        query = "SELECT nome, valor, categoria, data FROM dados"
        banco.c.execute(query)
        return banco.c.fetchall()
    
    def _buscar_tipo_categoria(self, categoria_nome):
        banco.c.execute("SELECT tipo FROM categorias WHERE categoria = ?", (categoria_nome,))
        resultado = banco.c.fetchone()
        return int(resultado[0]) if resultado else 0