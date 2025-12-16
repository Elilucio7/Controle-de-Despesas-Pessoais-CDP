from modules.cad_categ import cad_categ
from modules.despesa import despesa
from modules.receita import receita
from modules.orcamento import orcamento
from modules.relatorio import relatorio
from modules.config import config
import os

despesa_obj = despesa()
categoria_obj = cad_categ()
receita_obj = receita()
orcamento_obj = orcamento()
relatorio_obj = relatorio()
cfg = config()


if not os.path.exists("logs.txt"):
    with open(os.path.join("logs.txt"), "w", encoding="utf-8") as f:
        f.write("Log de Alertas do Sistema:\n")

while True:
    print("--Controle de Despesas Pessoais--\nEscolha qual ação deseja realizar\n1 - Criar categoria\n2 - Criar receita ou despesa\n3 - Ver dados de uma categoria\n4 - Atualizar Categoria\n5 - Ver itens cadastrados em uma categoria\n6 - Ver orçamento\n7 - Gerar relatório\n8 - Deletar categoria\n9 - Alterar configurações\n10 - Sair")
    while True:
        y = input()
        try:
            escolha = int(y)
            if escolha not in (1,2,3,4,5,6,7,8,9,10):
                print("Escolha de ação não válida, digite novamente: ")
            else:
                break
        except ValueError:
            print("Escolha de ação não válida, digite novamente: ")

            #sei da existência de switch case, mas quando estava trabalhando nessa parte não me lembrei, como já tinha escrito muito apenas com ifs e gastaria muito tempo com switch cases, preferi deixar assim(apenas quero esclarecer que sei que o código podia estar mais organizado)
            
    if escolha == 1:
        categoria_obj.cadastrar()
        
    elif escolha == 2:
        print("Selecione o tipo de item que será cadastrado (1 - Despesa, 2 - Receita): ")
        cat = str(input())
        while True:
            despesa_obj.ver_despesa()
            receita_obj.ver_receita()
            if cat == "1":
                print(despesa_obj.lista_despesa)
                despesa_obj.cadastrar_recdes()
                despesa_obj.cad_des()
                break
            elif cat == "2":
                print(receita_obj.lista_receita)
                receita_obj.cadastrar_recdes()
                receita_obj.cad_rec()
                break
            else:
                cat = str(input("Escolha inválida, digite 1 ou 2: "))
                
    elif escolha == 3:
        print("Categorias disponíveis:", cad_categ.lista_categorias)
        categoria_obj.ver_categ(input("Digite o nome da categoria para checagem: "))
        
    elif escolha == 4:
        categoria_obj.update_categ()

    elif escolha == 5:
        print("Categorias disponíveis:", cad_categ.lista_categorias)
        nome = str(input("Digite o nome da categoria para checagem de dados: "))
        while True:
            if nome in cad_categ.lista_categorias:
                tipo = cad_categ.lista_categorias[nome]
                if tipo == 1:
                    despesa_obj.ver_dado(nome)
                    break
                elif tipo == 2:
                    receita_obj.ver_dado(nome)
                    break
            else:
                nome = str(input("Categoria não cadastrada, digite novamente: "))
                
    elif escolha == 6:
        relatorio_obj._exibir_orcamento_mensal()
        
    elif escolha == 7:
        relatorio_obj.gerar_relatorios()
        
    elif escolha == 8:
        print("Categorias disponíveis:", cad_categ.lista_categorias)
        categoria_obj.del_categ()

    elif escolha == 9:
        cfg.menu_configuracao()
        
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