# language: pt
Funcionalidade: Carrinho de compras
  Como um usuário logado
  Quero gerenciar meu carrinho de compras
  Para controlar os itens antes de finalizar a compra

  Contexto:
    Dado que estou logado no sistema
    E adicionei um produto ao carrinho

  Cenário: Verificar item no carrinho
    Quando vou para o carrinho
    Então o carrinho deve conter ao menos 1 item

  Cenário: Remover item do carrinho
    Quando vou para o carrinho
    E removo o primeiro item
    Então o carrinho deve estar vazio

  Cenário: Continuar comprando após visitar o carrinho
    Quando vou para o carrinho
    E clico em Continuar Comprando
    Então devo estar na página de inventário
