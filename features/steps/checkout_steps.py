from behave import given, when, then
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@given("cliquei em Checkout")
def step_click_checkout(context):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    context.cart_page.checkout()
    context.checkout_page = CheckoutPage(context.driver)


@when('preencho os dados "{nome}" "{sobrenome}" "{cep}"')
def step_fill_checkout_info(context, nome, sobrenome, cep):
    nome      = "" if nome      == "(vazio)" else nome
    sobrenome = "" if sobrenome == "(vazio)" else sobrenome
    cep       = "" if cep       == "(vazio)" else cep
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_info(nome, sobrenome, cep)


@when("clico em Continue no checkout")
def step_click_continue_checkout(context):
    context.checkout_page.click_continue()


@when("clico em Cancel no checkout")
def step_click_cancel_checkout(context):
    context.checkout_page.click_cancel()


@when("clico em Finish")
def step_click_finish(context):
    context.checkout_page.click_finish()


@then('devo ver o erro de checkout "{mensagem}"')
def step_check_checkout_error(context, mensagem):
    actual = context.checkout_page.get_error_message()
    assert actual == mensagem, (
        f"Mensagem incorreta.\n  Esperado : '{mensagem}'\n  Obtido   : '{actual}'"
    )


@then('devo ver a confirmação "{mensagem}"')
def step_check_order_confirmation(context, mensagem):
    actual = context.checkout_page.get_complete_header()
    assert actual == mensagem, (
        f"Confirmação incorreta.\n  Esperado : '{mensagem}'\n  Obtido   : '{actual}'"
    )


@then("devo estar na página do carrinho")
def step_on_cart_page(context):
    assert "/cart.html" in context.driver.current_url, (
        f"URL esperada conter '/cart.html', atual: {context.driver.current_url}"
    )
