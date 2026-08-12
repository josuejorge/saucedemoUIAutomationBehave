# SauceDemo UI Automation — Behave

Automação de testes E2E com **Python + Behave + Selenium** para o site [https://www.saucedemo.com](https://www.saucedemo.com).

<img width="894" height="379" alt="image" src="https://github.com/user-attachments/assets/4e2df85f-6891-46bc-b846-a48c820c9239" />

<img width="1887" height="891" alt="image" src="https://github.com/user-attachments/assets/a7157d17-1c58-4e5a-aef4-dcab5a569fe6" />

---

## Tecnologias

| Tecnologia | Versão |
|---|---|
| Python | 3.14+ |
| Behave | 1.2.6 |
| Selenium | 4.27.0 |
| Behavex | latest (paralelismo) |
| Allure Behave | latest (relatórios) |
| Google Chrome | compatível com Selenium Manager |

---

## Pré-requisitos

- **Python 3.14+** instalado
- **Java 11+** instalado (necessário para o Allure CLI)
- **Allure CLI** instalado

Verificar instalações:

```bash
python --version
java -version
allure --version
```

---

## Instalação

```bash
pip install -r requirements.txt
```

---

## Estrutura do Projeto

```
saucedemoUIAutomationBehave/
├── features/
│   ├── login.feature       # 6 cenários
│   ├── home.feature        # 7 cenários
│   ├── cart.feature        # 3 cenários
│   ├── checkout.feature    # 5 cenários
│   ├── environment.py      # hooks: setup e teardown do Chrome por cenário
│   └── steps/
│       ├── login_steps.py
│       ├── home_steps.py
│       ├── cart_steps.py
│       └── checkout_steps.py
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── config/
│   └── config.py           # URL base e credenciais
├── behave.ini
├── requirements.txt
└── .gitignore
```

---

## Executando os Testes

### Rodar todos os testes (sequencial)

```bash
behave
```

### Rodar uma feature específica

```bash
behave features/login.feature
behave features/home.feature
behave features/cart.feature
behave features/checkout.feature
```

### Rodar um cenário específico (pelo número da linha)

```bash
behave features/login.feature:8
```

---

## Paralelismo

O projeto usa **Behavex** para rodar cenários em paralelo, cada um em uma instância separada do Chrome.

### Por cenário — até N cenários simultâneos

```bash
behavex --parallel-processes 4 --parallel-scheme scenario
```

### Por feature — um Chrome por feature file

```bash
behavex --parallel-processes 4 --parallel-scheme feature
```

O relatório HTML do Behavex é gerado automaticamente em `behavex-output/report.html`.

---

## Relatório Allure

### 1. Rodar os testes gerando os dados do Allure

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

### 2. Gerar o relatório HTML

```bash
allure generate allure-results -o allure-report --clean
```

### 3. Abrir no browser

```bash
allure open allure-report
```

### Gerar e abrir em um único comando

```bash
allure generate allure-results -o allure-report --clean && allure open allure-report
```

O relatório exibe todos os cenários agrupados por feature, o Gherkin de cada um (Dado / Quando / Então) e **screenshot automático anexado nos cenários que falharem**.

---

## Cenários de Teste

### Login — 6 cenários
- Login com credenciais válidas
- Login com credenciais inválidas
- Login com campos vazios
- Login com usuário bloqueado
- Login com different tipos de usuários (Esquema do Cenário — 2 linhas)

### Home — 7 cenários
- Homepage carregada após login
- 6 produtos exibidos no inventário
- Adicionar produto ao carrinho (badge = 1)
- Ordenação A → Z
- Ordenação Z → A
- Ordenação preço menor → maior
- Ordenação preço maior → menor

### Carrinho — 3 cenários
- Item adicionado aparece no carrinho
- Remover item do carrinho
- Continuar comprando após visitar o carrinho

### Checkout — 5 cenários
- Campo nome obrigatório
- Campo sobrenome obrigatório
- Campo CEP obrigatório
- Cancelar o checkout
- Finalizar compra com sucesso

**Total: 21 cenários automatizados**

---

## Como o BDD funciona neste projeto

Cada teste é escrito em **Gherkin** (linguagem natural em português) e conectado a código Python via decoradores `@given`, `@when`, `@then`:

```gherkin
Cenário: Login com credenciais válidas
  Dado que estou na página de login
  Quando faço login com "standard_user" e "secret_sauce"
  Então devo ser redirecionado para a página de inventário
```

O `Contexto:` (Background) evita repetição — os features de Home, Carrinho e Checkout usam `Dado que estou logado no sistema` como pré-condição comum a todos os cenários.
