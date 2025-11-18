# Controle-de-Despesas-Pessoais-CDP
Projeto para a cadeira de P.O.O. no segundo semestre de engenharia de software

Ele tem como objetivo de construir um sistema de linha de comando (CLI) para gerenciar receitas, despesas e orçamentos pessoais, com armazenamento persistente em JSON ou SQLite com foco em aplicar encapsulamento, herança, métodos especiais, validações rigorosas e relações entre múltiplas classes.

  ESPECIFICAÇÃO PROJETO 1 - POO    
  TEMA 5 – SISTEMA DE CONTROLE DE DESPESAS PESSOAIS    
  UML Textual
  
Cadastro de categoria   
  Atributos   
    1. nome   
    2. tipo (receita/despesa)   
    3. limite mensal   
    4. descrição opcional   
  Métodos  
    1. criar categorias  
    2. remover categorias  
    3. dar update em categorias  
    4. impedir duplicidade de nomes  
    Relações:  
    Usuário cadastrar categoria de receita ou despesa com suas caraacterísticas  
    Usuário remover categorias  
    Usuário atualizar informações nas categorias  
  
Lançamento de receitas e despesas  
  Atributos  
    1. valor  
    2. Categoria  
    3. data  
    4. descrição (opcional)  
    5. forma de pagamento (caso despesa)  
  Métodos  
    1. criar despesas e receitas  
    2. editar receitas e despesas  
    3. remover receitas e despesas  
    4. impedir lançamento com valor ≤ 0  
  Relacões:  
Usuário criar despesas e receitas  
Usuário editar receitas e despesas  
Usuário remover receitas e despesas  

Orçamento  
  Atributos  
    1. Categorias  
    2. saldo_disponível  
    3. total_de_receitas (calculado à partir das receitas registradas no banco de dados)  
    4. total_de_despesas (calculado à partir das despesas registradas no banco de dados)  
    5. saldo_mensal  
  Métodos  
    1. cálculo do total de receitas e despesas  
    2. cálculo do saldo diário e mensal e dos totais (receita e despesa)  
  Relações:  
  Disponibilizar saldos diario e mensal além dos totais das receitas e despesas para os demais módulos  

Relatórios e estatísticas  
  Atributos  
    1. Categorias de despesa  
    2. Orçamento.saldo_mensal  
    3. Orçamento.total_de_despesas  
    4. despesas (obtidas do banco de dados)  
    5. receitas (obtidas do banco de dados)  
    6. data_de_despesa  
    7. meses_comparar  
    8. n_meses (usado para comparar receitas e despesas)  
  Métodos  
    1. agrupar despesas por forma de pagamento  
    2. calcular percentual de cada categoria em relação ao total de despesas  
    3. calcular o mês mais econômico  
    4. comparar as receitas e despesas dos últimos n meses  
    5. gerar relatório demonstrando os cálculos realisados pela classe, o agrupamento e a comparação e também os totais de despesas e receitas feitos pelo orçamento  
  Relações:  
  Demonstra ao usuário todos os processos realizados em formato de relatório  
    
Alertas automáticos  
  Atributos  
    1. Categoria_despesa  
    2. despesas (obtidas do banco de dados)  
    3. minimo_des  
  Métodos
    1. alerta de valor alto para despesas acima de R$500  
    2. alerta de limite excedido para despesas que ultrapassam limite de categoria  
    3. alerta de déficit orçamentário para saldo mensal negativo  
  Relações:  
  Alerta o Usuário para cada caso especificado  
    
Configurações  
  Atributos  
    1. Alerta.minimo_des  
    2. Relatorio.n_meses  
    3. meta  
  Métodos  
    1. alterar valor mínimo para alerta de despesa (minimo_des)  
    2. alterar número de meses de comparativo (n_meses)  
    3. definir meta mensal de economia  
  Relações:  
  Permite alterar alguns valores de outras classes, especificado nos métodos (como n_meses)  
  
