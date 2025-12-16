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
                    data text,
                    descricao text,
                    forma_pagamento text
        )""")
        self.conn.commit()

    def listar_categorias(self):
        self.c.execute("SELECT categoria, tipo FROM categorias")
        return {row[0]: int(row[1]) for row in self.c.fetchall()}

    def inserir_categoria(self, tipo, categoria, limite, descricao):
        self.c.execute("INSERT INTO categorias (tipo, categoria, limite, descricao) VALUES (?, ?, ?, ?)",
                (tipo, categoria, limite, descricao))
        self.conn.commit()

    def inserir_dado(self, nome, valor, categoria, data, descricao, forma_pagamento):
        self.c.execute("INSERT INTO dados (nome, valor, categoria, data, descricao, forma_pagamento) VALUES (?, ?, ?, ?, ?, ?)",
                       (nome, valor, categoria, data, descricao, forma_pagamento))
        self.conn.commit()

    def atualizar_categoria(self, nome_antigo, novo_tipo, novo_limite, nova_descricao):
        try:
            self.c.execute("""
                UPDATE categorias
                SET tipo=?, limite=?, descricao=?
                WHERE categoria=?
            """, (novo_tipo, novo_limite, nova_descricao, nome_antigo))
            self.conn.commit()

        except Exception:
            self.conn.rollback()

    def buscar_categoria(self, categoria_nome):
        self.c.execute("SELECT tipo, categoria, limite, descricao FROM categorias WHERE categoria = ?", (categoria_nome,))
        return self.c.fetchone()

    def buscar_limite_categoria(self, categoria_nome):
        self.c.execute("SELECT limite FROM categorias WHERE categoria = ?", (categoria_nome,))
        resultado = self.c.fetchone()
        if resultado:
            return resultado[0]
        return None

    def somar_gastos_categoria(self, categoria_nome):
        self.c.execute("SELECT SUM(valor) FROM dados WHERE categoria = ?", (categoria_nome,))
        resultado = self.c.fetchone()
        return resultado[0] if resultado[0] else 0.0

    def buscar_dados(self, categoria):
        self.c.execute("SELECT nome, valor, data, descricao, forma_pagamento FROM dados WHERE categoria=?", (categoria,))
        return self.c.fetchall()

    def deletar_categ(self, categoria):
        self.c.execute("DELETE FROM dados WHERE categoria=?", (categoria,))
        self.c.execute("DELETE FROM categorias WHERE categoria=?", (categoria,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()