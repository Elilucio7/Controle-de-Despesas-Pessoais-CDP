import modules.bancodados as bancodados

banco = bancodados.BancoDados()
class cad_categ:
    limite_usado = 10
    se_cadastrando = False
    lista_categorias = banco.listar_categorias() 
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

    def listar_e_selecionar(self):
        categorias_db = banco.listar_categorias()
        if not categorias_db:
            print("Não há categorias cadastradas para atualizar.")
            return None
        print("\nCategorias disponíveis:")
        for i, cat in enumerate(categorias_db):
            print(f"[{i+1}] {cat}")
        while True:
            try:
                escolha = int(input("Digite o número da categoria que deseja atualizar: ")) - 1
                if 0 <= escolha < len(categorias_db):
                    return categorias_db[escolha]
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def tentar_valor(self, valor_antes, valor):
        if valor == "1":
            while True:
                try:
                    valor_antes = float(valor_antes)
                    if valor_antes >= 0:
                        break
                    else:
                        print("Valor inválido. Digite novamente: ")
                        valor_antes = input()
                except ValueError:
                    print("Valor inválido. Digite novamente: ")
                    valor_antes = input()
            return valor_antes
        elif valor == "2":
            while True:
                try:
                    valor_antes = int(valor_antes)
                    break
                except ValueError:
                    print("Valor inválido. Digite novamente: ")
                    valor_antes = input()
            return valor_antes
    
    def cad(self, nome_antigo = None):
        print("Digite os dados da categoria\n")
        print("Nome da categoria: ")
        while True:
            self.__categoria = str(input())
            if self.__categoria in self.lista_categorias and self.se_cadastrando:
                return print("Categoria já cadastrada.")
            elif self.__categoria in self.lista_categorias and not self.se_cadastrando:
                print("Categoria com nome existente. Digite novamente: ")
            else:
                break
        print("\n", "Tipo da categoria (despesa = 1 ou receita = 2): ")
        self.__tipo = self.tentar_valor(input(), "2")
        while self.__tipo != 1 and self.__tipo != 2:
                self.__tipo = self.tentar_valor(input(), "2")
                print("Tipo inválido. Digite novamente (despesa = 1 ou receita = 2): ")
        self.lista_categorias[self.__categoria] = self.__tipo
        if self.__tipo == 1:
            print("\n", "Limite monetário da categoria: ")
            while True:
                limite_input = input()
                if not limite_input:
                    self._limite = self.limite_usado
                    break
                try:
                    limite_float = float(limite_input)
                    if limite_float <= 0:
                        print("O limite deve ser positivo. Digite novamente: ")
                    else:
                        self._limite = limite_float
                        break
                except ValueError:
                    print("Limite inválido. Digite um número: ")
        else:
            self.limite = 0.0
        print("\n", "Descrição da categoria: ")
        self.desc = str(input())
        self.lista_categorias[self.__categoria] = self.__tipo
        if self.se_cadastrando:
            print("\n", "Categoria cadastrada com sucesso.")
            banco.inserir_categoria(self.__tipo, self.__categoria, self._limite, self.__desc)
        elif nome_antigo:
            print("\n", "Categoria atualizada com sucesso!")
            banco.atualizar_categoria(nome_antigo=nome_antigo, novo_nome=self.__categoria,novo_tipo=self.__tipo, novo_limite=self._limite, nova_descricao=self.__desc)
        else:
            print("\n", "Categoria atualizada com sucesso.")
            banco.atualizar_categoria(self.__categoria, self.__tipo, self._limite, self.__desc)


    def cadastrar(self):
        self.se_cadastrando = True
        self.cad()
    
    def ver_categ(self, x):
       banco.buscar_categoria(x)

    def update_categ(self):
        self.se_cadastrando = False
        nome_antigo = self.listar_e_selecionar()
        if nome_antigo:
            dados_antigos = banco.buscar_categoria(nome_antigo)
            if dados_antigos:
                self.__tipo, self.__categoria, self._limite, self.__desc = dados_antigos
                print(f"\n--- Editando Categoria: {self.__categoria} ({self.__tipo}) ---")
                self.cad(nome_antigo) 
        else:
            print("Nenhuma categoria selecionada.")
        del self.lista_categorias[self.__categoria]
        del self.lista_limites[self.__categoria]

    def del_categ(self):
        if self.__categoria in self.lista_categorias:
            del self.lista_categorias[self.__categoria]
            print(f"Categoria {self.__categoria} deletada com sucesso.")
            banco.deletar_categ(self.__categoria)
        else:
            print("Categoria não encontrada.")
        

"""Essa classe será ultilizada para cadastrar categorias de despesas e receitas, assim como editá-las."""
