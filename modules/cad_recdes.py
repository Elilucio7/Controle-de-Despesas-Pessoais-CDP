from modules.cad_categ import cad_categ

class cad_recdes(cad_categ):
    lista_categorias = cad_categ.lista_categorias
    lista_dados = {"açaí": 1, "aluguel": 1, "salário": 2}
    def __init__(self, nome = None, tipo = None, valor = None, data = None, categoria = None, limite = None):
        super().__init__(tipo)
        self.categoria = cad_categ(categoria)
        self._nome = nome
        self.valor = valor
        self.data = data
        self.limite = cad_categ.limite_usado


    def __str__(self):
        return f"Nome: {self._nome}, Tipo: {'receita' if self.tipo == 2 else 'despesa'}, Valor: {self.valor}, Data: {self.data}, Categoria: {self.get_categ}, Limite: {self.limite}"
    
    def __contains__(self):
        return self.nome in self.lista_categorias

    def cad_rec():
        print("Digite o nome da receita: ")

    def cadastrar_recdes(self):
        print("Selecione a categoria para cadastro: \n")
        print(self.lista_categorias)
        while True:
            self.categoria = str(input())
            if self.categoria in self.lista_categorias:
                break
            else:
                print("Categoria não encontrada! Digite novamente: ")
        self.tipo = self.lista_categorias[self.categoria]
        print(self.tipo)
        if self.tipo == 1:
            pass #implementar despesa main
        elif self.tipo == 2:
            pass #implementar receita main

    def ver_dado(self):
        print(self)


