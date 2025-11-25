from modules.cad_categ import cad_categ

#criando objetos
despesa = cad_categ()
despesa.cadastrar()
receita = cad_categ()
receita.cadastrar()

#vendo os objetos criados
despesa.ver_categ()
receita.ver_categ()

#editando objetos
despesa.update_categ()
receita.update_categ()

#"deletando" objetos
despesa.del_categ()
receita.del_categ()

#vendo os objetos deletados causa erro
try:
    receita.ver_categ()
except AttributeError:
    print("Receita deletada com sucesso!")
