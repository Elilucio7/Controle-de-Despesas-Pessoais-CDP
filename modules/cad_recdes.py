from modules.cad_categ import cad_categ
import modules.bancodados as bancodados

banco = bancodados.BancoDados()

class cad_recdes(cad_categ):
    lista_categorias = cad_categ.lista_categorias
    lista_dados = {}
    def __init__(self, nome = None, tipo = None, valor = None, data = None, categoria = None, limite = None):
        super().__init__(tipo)
        self.categoria = cad_categ(categoria)
        self._nome = nome
        self.valor = valor
        self.data = data
        self.limite = limite
        self.descricao = None
        self.forma_pagamento = None

    def listar_despesas(tipo = 1):
        banco.c.execute("SELECT categoria FROM categorias WHERE tipo=?", (tipo,))
        return [row[0] for row in banco.c.fetchall()]

    def listar_receitas(tipo = 2):
        banco.c.execute("SELECT categoria FROM categorias WHERE tipo=?", (tipo,))
        return [row[0] for row in banco.c.fetchall()]

    def cadastrar_recdes(self):
        self.lista_categorias = banco.listar_categorias()
        print("Digite o nome da categoria: ")
        while True:
            self.categoria = str(input())
            if self.categoria in self.lista_categorias:
                break
            else:
                print("Categoria não encontrada! Digite novamente: ")
        self.tipo = self.lista_categorias[self.categoria]
        if self.tipo == 1:
            self.limite = banco.buscar_limite_categoria(self.categoria)
        else:
            self.limite = None

    def ver_dado(self, x):
        dados = banco.buscar_dados(x)
        if dados:
            tipo_nome = 'Despesa' if self.tipo == 1 else 'Receita' 
            print(f"\n--- Dados de {tipo_nome}s em '{x}' ---")
            for nome, valor, data, descricao, forma_pagamento in dados:
                print(f"Nome: {nome} | Valor: R${valor:.2f} | Data: {data} | Desc: {descricao} | Pagamento: {forma_pagamento}")
        else:
            print(f"Nenhum dado encontrado para a categoria '{x}'.")

            