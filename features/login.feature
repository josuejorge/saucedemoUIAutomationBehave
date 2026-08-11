# language: pt
Funcionalidade: Login no SauceDemo
  Como um usuário registrado
  Quero fazer login no site
  Para acessar o inventário de produtos

  Cenário: Login com credenciais válidas
    Dado que estou na página de login
    Quando faço login com "standard_user" e "secret_sauce"
    Então devo ser redirecionado para a página de inventário

  Cenário: Login com credenciais inválidas
    Dado que estou na página de login
    Quando faço login com "usuario_errado" e "senha_errada"
    Então devo ver a mensagem de erro "Epic sadface: Username and password do not match any user in this service"

  Cenário: Login com campos vazios
    Dado que estou na página de login
    Quando clico em Login sem preencher os campos
    Então devo ver a mensagem de erro "Epic sadface: Username is required"

  Cenário: Login com usuário bloqueado
    Dado que estou na página de login
    Quando faço login com "locked_out_user" e "secret_sauce"
    Então devo ver a mensagem de erro "Epic sadface: Sorry, this user has been locked out."

  Esquema do Cenário: Login com diferentes tipos de usuários
    Dado que estou na página de login
    Quando faço login com "<usuario>" e "secret_sauce"
    Então devo ser redirecionado para a página de inventário

    Exemplos:
      | usuario           |
      | standard_user     |
      | performance_glitch_user |
