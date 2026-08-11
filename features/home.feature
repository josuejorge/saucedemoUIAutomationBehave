# language: pt
Funcionalidade: Página inicial do SauceDemo
  Como um usuário logado
  Quero visualizar e interagir com os produtos
  Para navegar pelo catálogo da loja

  Contexto:
    Dado que estou logado no sistema

  Cenário: Verificar homepage carregada
    Então devo ver a lista de produtos

  Cenário: Verificar quantidade de produtos exibidos
    Então devo ver 6 produtos no inventário

  Cenário: Adicionar produto ao carrinho
    Quando adiciono o primeiro produto ao carrinho
    Então o badge do carrinho deve exibir "1"

  Esquema do Cenário: Ordenar produtos por diferentes critérios
    Quando ordeno os produtos por "<ordenacao>"
    Então os produtos devem estar ordenados corretamente por "<ordenacao>"

    Exemplos:
      | ordenacao |
      | az        |
      | za        |
      | lohi      |
      | hilo      |
