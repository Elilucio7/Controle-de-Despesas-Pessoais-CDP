from modules.cad_categ import cad_categ
from modules.despesa import despesa


#criando objetos
despesa = despesa()
categoria = cad_categ()

categoria.cadastrar()
despesa.cadastrar_recdes()
despesa.cad_des()

despesa.ver_dado()
categoria.ver_categ()

categoria.del_categ()