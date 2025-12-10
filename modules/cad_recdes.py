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
        self.limite = cad_categ.limite_usado

    def listar_despesas(tipo = "1"):
        banco.c.execute("SELECT categoria FROM categorias WHERE tipo=?", (tipo))
        return [row for row in banco.c.fetchall()]

    def listar_receitas(tipo = "2"):
        banco.c.execute("SELECT categoria FROM categorias WHERE tipo=?", (tipo))
        return [row for row in banco.c.fetchall()]

    def __str__(self):
        return f"Nome: {self._nome}, Tipo: {'receita' if self.tipo == 2 else 'despesa'}, Valor: {self.valor}, Data: {self.data}, Categoria: {self.get_categ}, Limite: {self.limite}"
    
    def __contains__(self):
        return self.nome in self.lista_categorias

    def cadastrar_recdes(self):
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
            print(f"\n--- Dados de {tipo_nome} para a Categoria: {self.categoria} ---")
            
            for nome, valor, data in dados:
                print(f"  {nome} (Data: {data}): R${valor:.2f}") 
        else:
            print(f"Nenhum dado encontrado para a categoria {self.categoria}.")



