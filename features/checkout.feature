# language: pt
Funcionalidade: Checkout de compras
  Como um usuário com itens no carrinho
  Quero finalizar minha compra
  Para receber os produtos em casa

  Contexto:
    Dado que estou logado no sistema
    E adicionei um produto ao carrinho
    E fui para o carrinho
    E cliquei em Checkout

  Esquema do Cenário: Validar campos obrigatórios do checkout
    Quando preencho os dados "<nome>" "<sobrenome>" "<cep>"
    E clico em Continue no checkout
    Então devo ver o erro de checkout "<mensagem>"

    Exemplos:
      | nome    | sobrenome | cep    | mensagem                       |
      | (vazio) | Silva     | 12345  | Error: First Name is required  |
      | João    | (vazio)   | 12345  | Error: Last Name is required   |
      | João    | Silva     | (vazio)| Error: Postal Code is required |

  Cenário: Cancelar o checkout
    Quando clico em Cancel no checkout
    Então devo estar na página do carrinho

  Cenário: Finalizar compra com sucesso
    Quando preencho os dados "João" "Silva" "12345"
    E clico em Continue no checkout
    E clico em Finish
    Então devo ver a confirmação "Thank you for your order!"
