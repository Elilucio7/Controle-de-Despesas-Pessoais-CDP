class cad_categ:
    se_cadastrando = False
    lista_categorias = {"q": 2}
    def __init__(self, tipo = None, categoria = None, limite = None, desc = None):
        self.__tipo = tipo
        self.__categoria = categoria
        self._limite = limite
        self.__desc = desc

    @property  
    def get_tipo(self):
        return self.__tipo
    @get_tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def get_categ(self):
        return self.__categoria
    @get_categ.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def get_desc(self):
        return self.__desc
    @get_desc.setter
    def desc(self, desc):
        self.__desc = desc

    def tentar_valor(self, valor_antes, valor):
        if valor == "1":
            while True:
                try:
                    valor_antes = float(valor_antes)
                    break
                except ValueError:
                    print("Valor inválido! Digite novamente: ")
                    valor_antes = input()
            return valor_antes
        elif valor == "2":
            while True:
                try:
                    valor_antes = int(valor_antes)
                    break
                except ValueError:
                    print("Valor inválido! Digite novamente: ")
                    valor_antes = input()
            return valor_antes
    
    def cad(self):
        print("Digite os dados da categoria\n")
        print("Nome da categoria: ")
        nome_antes = str(input())
        if nome_antes in self.lista_categorias: #será alterado quando o banco de dados for implementado
            if self.se_cadastrando:
                return print("Categoria já cadastrada!")
            else:
                return print("Categoria não pode ser atualizada para um nome já existente!")
        else:
            self.__categoria = nome_antes
        print("\n", "Tipo da categoria (despesa = 1 ou receita = 2): ")
        tipo_antes = self.tentar_valor(input(), "2")
        while tipo_antes != 1 and tipo_antes != 2:
                tipo_antes = self.tentar_valor(input(), "2")
                print("Tipo inválido! Digite novamente (despesa = 1 ou receita = 2): ")
        self.__tipo = tipo_antes
        self.lista_categorias[self.__categoria] = self.__tipo
        print("\n", "Limite monetário da categoria: ")
        limite_antes = self.tentar_valor(input(), "1")
        self._limite = limite_antes
        print("\n", "Descrição da categoria: ")
        self.desc = str(input())
        if self.se_cadastrando:
            print("\n", "Categoria cadastrada com sucesso!")
        else:
            print("\n", "Categoria atualizada com sucesso!")


    def cadastrar(self):
        self.se_cadastrando = True
        self.cad()
    
    def ver_categ(self):
        print(f"Categoria: {self.__categoria}\nTipo: {self.__tipo}\nLimite: {self._limite}\nDescrição: {self.__desc}")

    def update_categ(self):
        self.se_cadastrando = False
        self.cad()

    def del_categ(self):
        if self.__categoria in self.lista_categorias:
            del self.lista_categorias[self.__categoria]
            print(f"Categoria {self.__categoria} deletada com sucesso!")
            del self.__categoria
            del self.__tipo 
            del self._limite
            del self.__desc 
            
        else:
            print("Categoria não encontrada!")
        

"""Essa classe será ultilizada para cadastrar categorias de despesas e receitas, assim como editá-las."""
