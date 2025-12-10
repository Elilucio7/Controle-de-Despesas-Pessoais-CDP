from modules.cad_categ import cad_categ
from modules.despesa import despesa
from modules.receita import receita
from modules.orcamento import orcamento
from modules.relatorio import relatorio

#criando objetos
despesa_obj = despesa()
categoria = cad_categ()
receita_obj = receita()
orcamento_obj = orcamento()
relatorio_obj = relatorio()

while True:
    print("--Controle de Despesas Pessoais--\nEscolha qual ação deseja realizar\n1 - Criar categoria\n2 - Criar receita ou  despesa\n3 - Ver dados de uma categoria\n4 - Ver itens cadastrados em uma categoria\n5 - Ver orçamento\n6 - Gerar relatório\n7 - Deletar categoria(ainda não implementado corretamente, deleta a última categoria iterada)\n8 - Sair")
    while True:
        y = input()
        escolha = cad_categ.tentar_valor(y,y,"2")
        if escolha not in [1,2,3,4,5,6,7]:
            print("Escolha de ação não válida, digite novamente: ")
        else:
            break
    if escolha == 1:
        categoria.cadastrar()
    elif escolha == 2:
        print("Selecione o tipo de item que será cadastrado: ")
        cat = str(input())
        while True:
                if cat == "1":
                    print("Selecione a categoria para cadastro: \n")
                    print(despesa.lista_despesa)
                    despesa_obj.cadastrar_recdes()
                    despesa_obj.cad_des()
                    break
                elif cat == "2":
                    print("Selecione a categoria para cadastro: \n")
                    print(receita.lista_receita)
                    receita_obj.cadastrar_recdes()
                    receita_obj.cad_rec()
                    break
                else:
                    cat = str(input("Categoria não presente, digite novamente: "))
    elif escolha == 3:
        name = str(input("Digite o nome da categoria para checagem: "))
        print(cad_categ.lista_categorias)
        categoria.ver_categ(name)
    elif escolha == 4:
        print(cad_categ.lista_categorias)
        nome = str(input("Digite o nome da categoria para checagem de dados: "))
        print(cad_categ.lista_categorias)
        while True:
            if nome in cad_categ.lista_categorias:
                tipo = cad_categ.lista_categorias[nome]
                if tipo == 1:
                    despesa_obj.ver_dado()
                    break
                elif tipo == 2:
                    receita_obj.ver_dado()
                    break
            else:
                nome = str(input("Categoria não cadastrada, digite novamente: "))
    elif escolha == 5:
        orcamento.calcular_e_exibir_orcamento()
    elif escolha == 6:
        relatorio.gerar_relatorios()
    elif escolha == 7:
        categoria.del_categ()
    else:
        break

#categoria.cadastrar()
#despesa.cadastrar_recdes()
#despesa.cad_des()
#receita.cadastrar_recdes()
#receita.cad_rec()

#receita.ver_dado()
#despesa.ver_dado()
#categoria.ver_categ()

#orcamento.calcular_e_exibir_orcamento()
#relatorio.gerar_relatorios()