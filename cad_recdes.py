import cad_categ

class cad_recdes(cad_categ.cad_categ):
    lista_categorias = cad_categ.cad_categ.lista_categorias
    def __init__(self, nome = None, tipo = None, valor = None, data = None, categoria = None, limite = None):
        super().__init__(tipo)
        self.categoria = cad_categ.cad_categ(categoria)
        self.limite = cad_categ.cad_categ(limite)
        self._nome = nome
        self.valor = valor
        self.data = data

    def __str__(self):
        return f"Nome: {self._nome}, Tipo: {'receita' if self.get_tipo == 2 else 'despesa'}, Valor: {self.valor}, Data: {self.data}, Categoria: {self.get_categ}"
    
    def __contains__(self, nome):
        return self.nome in self.lista_categorias

    def cad_des():
        pass  # Lógica para cadastrar despesa, implementada futuramente
    def cad_rec():
        pass  # Lógica para cadastrar receita, implementada futuramente

    def cadastrar_recdes(self):
        print("Selecione a categoria para cadastro: \n")
        print(self.lista_categorias)
        while True:
            self.__categoria = str(input())
            if self.__categoria in self.lista_categorias:
                break
            else:
                print("Categoria não encontrada! Digite novamente: ")
        if self.get_tipo == 1:
            self.cad_des()
        elif self.get_tipo == 2:
            self.cad_rec()

class receita(cad_recdes):
    def __init__(self, nome = None, valor = None, categoria = None):
        cad_recdes.cad_recdes.cadastrar_recdes(self)
        super().__init__( 2, valor, None, categoria, None)
        self.nome = nome #será implementado para ser pego no banco de dados

import cad_recdes
class despesa(cad_recdes):
    def __init__(self, nome = None, valor = None, categoria = None):
        cad_recdes.cad_recdes.cadastrar_recdes(self)
        super().__init__( 1, valor, None, categoria, None)
        self.nome = nome #será implementado para ser pego no banco de dados