import modules.bancodados as bancodados

banco = bancodados.BancoDados()
class cad_categ:
    limite_usado = 10
    se_cadastrando = False
    lista_categorias = banco.listar_categorias() 
    lista_limites = {}

    def __init__(self, tipo = None, categoria = None, limite = None, desc = None):
        self.__tipo = tipo
        self.__categoria = categoria
        self._limite = limite
        self.__desc = desc

#properties não usados, existem por questão de eu não ter aprendido no entregável relacionado à primeira iteração do cad_categ

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
    def get_limite(self):
        return self._limite
    @get_limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def get_desc(self):
        return self.__desc
    @get_desc.setter
    def desc(self, desc):
        self.__desc = desc

    def listar_e_selecionar(self):
        if not self.lista_categorias:
            print("Não há categorias cadastradas para atualizar.")
            return None
        print("\nCategorias disponíveis:")
        categorias_list = list(self.lista_categorias.keys())
        for i, cat in enumerate(categorias_list):
            tipo = "RECEITA" if self.lista_categorias[cat] == 2 else "DESPESA"
            print(f"[{i+1}] {cat} ({tipo})")
        while True:
            try:
                escolha = input("Selecione o número da categoria: ")
                indice = int(escolha) - 1
                if 0 <= indice < len(categorias_list):
                    return categorias_list[indice]
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def tentar_valor(self, y, x):
        while True:
            try:
                if x == "1":
                    return float(y)
                elif x == "2":
                    return int(y)
            except ValueError:
                y = input("Valor inválido! Digite novamente: ")

    def cad(self, nome_antigo=None):
        if self.se_cadastrando:
            print("Digite o tipo da categoria (1 - Despesa, 2 - Receita): ")
            while True:
                self.tipo = self.tentar_valor(input(), "2")
                if self.tipo in [1, 2]:
                    break
                else:
                    print("Tipo inválido. Digite 1 (Despesa) ou 2 (Receita): ")

            print("Digite o nome da categoria: ")
            while True:
                self.categoria = str(input()).strip()
                if self.categoria in self.lista_categorias:
                    print("Categoria já cadastrada! Digite novamente: ")
                else:
                    break
            
            self._limite = 0.0
            if self.tipo == 1:
                print("Digite o limite mensal para esta despesa (R$): ")
                self._limite = self.tentar_valor(input(), "1")
                while self._limite <= 0:
                    print("O limite não pode ser negativo ou igual a zero. Digite novamente: ")
                    self._limite = self.tentar_valor(input(), "1")
                    
            print("Digite a descrição opcional da categoria: ")
            self.__desc = str(input())
            banco.inserir_categoria(self.tipo, self.categoria, self._limite, self.__desc)
            self.lista_categorias[self.categoria] = self.tipo
            print("\n", "Categoria cadastrada com sucesso.")
            
        else: 
            print(self.__tipo)
            if self.__tipo == "1":
                novo_limite = self.tentar_valor(input(f"Digite o novo limite mensal (R$, Atual: R${self._limite:.2f}): "), "1")
            else:
                novo_limite = 0.0
            if self.__tipo == 1:
                print(f"Digite o novo limite mensal (R$, 0 para manter - Atual: R${self._limite:.2f}): ")
                limite_input = input()
                if limite_input:
                    novo_limite = self.tentar_valor(limite_input, "1")
                    while novo_limite < 0:
                        print("O limite não pode ser negativo. Digite novamente: ")
                        novo_limite = self.tentar_valor(input(), "1")
            
            print(f"Digite a nova descrição opcional (Enter para manter - Atual: {self.__desc}): ")
            nova_desc = input()
            if nova_desc:
                self.__desc = nova_desc

            banco.atualizar_categoria(nome_antigo, self.__tipo, novo_limite, self.__desc)
            self._limite = novo_limite
            self.lista_categorias[nome_antigo] = self.__tipo
            print("\n", "Categoria atualizada com sucesso.")


    def cadastrar(self):
        self.se_cadastrando = True
        self.cad()
    
    def ver_categ(self, x):
        dados = banco.buscar_categoria(x)
        if dados:
            tipo, nome, limite, descricao = dados
            tipo_str = "RECEITA" if tipo == 2 else "DESPESA"
            print("\n--- DETALHES DA CATEGORIA ---")
            print(f"Nome: {nome}")
            print(f"Tipo: {tipo_str}")
            print(f"Limite Mensal: R${limite:.2f}")
            print(f"Descrição: {descricao}")
        else:
            print(f"Categoria '{x}' não encontrada.")

    def update_categ(self):
        self.se_cadastrando = False
        nome_antigo = self.listar_e_selecionar()
        if nome_antigo:
            dados_antigos = banco.buscar_categoria(nome_antigo)
            if dados_antigos:
                self.__tipo, self.__categoria, self._limite, self.__desc = dados_antigos
                print(self.__tipo)
                print(f"\n--- Editando Categoria: {self.__categoria} ---")
                self.cad(nome_antigo) 
        else:
            print("Nenhuma categoria selecionada.")

    def del_categ(self):
        self.__categoria = str(input("Digite o nome da categoria que deseja deletar: "))
        if self.__categoria in self.lista_categorias:
            del self.lista_categorias[self.__categoria]
            banco.deletar_categ(self.__categoria)
            print(f"Categoria {self.__categoria} deletada com sucesso.")
        else:
            print("Categoria não encontrada.")
        


