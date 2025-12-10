import sqlite3

class BancoDados:
    def __init__(self, db_name='dados.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS categorias (
                  tipo text,
                    categoria text,
                    limite real,
                    descricao text
        )""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS dados (
                  nome text,
                    valor real,
                    categoria text,
                    data text
        )""")
        self.conn.commit()

    def listar_categorias(self):
        self.c.execute("SELECT categoria, tipo FROM categorias")
        return {row[0]: row[1] for row in self.c.fetchall()}

    def inserir_categoria(self, tipo, categoria, limite, descricao):
        self.c.execute("INSERT INTO categorias (tipo, categoria, limite, descricao) VALUES (?, ?, ?, ?)",
                (tipo, categoria, limite, descricao))
        self.conn.commit()

    def inserir_dado(self, nome, valor, categoria, data):
        self.c.execute("INSERT INTO dados (nome, valor, categoria, data) VALUES (?, ?, ?, ?)",
                       (nome, valor, categoria, data))
        self.conn.commit()

    def atualizar_categoria(self, nome_antigo, novo_nome, novo_tipo, novo_limite, nova_descricao):
        try:
            self.c.execute("""
                UPDATE categorias 
                SET tipo=?, categoria=?, limite=?, descricao=? 
                WHERE categoria=?
            """, (novo_tipo, novo_nome, novo_limite, nova_descricao, nome_antigo))
            if nome_antigo != novo_nome:
                self.c.execute(""" UPDATE dados SET categoria=? WHERE categoria=?""",
                     (novo_nome, nome_antigo))
            self.c.execute("""
                DELETE FROM dados 
                WHERE categoria=? AND valor < ?
            """, (novo_nome, novo_limite)).rowcount
            print("Os dados armazenados na categoria abaixo do novo limite foram apagados.")
            self.conn.commit()
            print(f"Categoria atualizada de '{nome_antigo}' para '{novo_nome}' com sucesso.")
            
        except Exception:
            self.conn.rollback()
            print("Erro ao atualizar")

    def buscar_categoria(self, categoria_nome):
        self.c.execute("SELECT tipo, categoria, limite, descricao FROM categorias WHERE categoria = ?", (categoria_nome,))
        return print(self.c.fetchone())

    def buscar_limite_categoria(self, categoria_nome):
        self.c.execute("SELECT limite FROM categorias WHERE categoria = ?", (categoria_nome,))
        resultado = self.c.fetchone()
        if resultado:
            return resultado[0]
        return None

    def buscar_dados(self, categoria):
        self.c.execute("SELECT nome, valor, data FROM dados WHERE categoria=?", (categoria,))
        return self.c.fetchall()

    def deletar_categ(self, categoria):
        self.c.execute("DELETE FROM dados WHERE categoria=?", (categoria,))
        self.c.execute("DELETE FROM categorias WHERE categoria=?", (categoria,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()


