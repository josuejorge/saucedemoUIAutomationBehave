from behave import given, when, then
from pages.login_page import LoginPage
from config.config import USERNAME, PASSWORD


@given("que estou logado no sistema")
def step_logged_in_with_defaults(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()
    context.login_page.login(USERNAME, PASSWORD)


@given("que estou na página de login")
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()


@when('faço login com "{usuario}" e "{senha}"')
def step_do_login(context, usuario, senha):
    context.login_page.login(usuario, senha)


@when("clico em Login sem preencher os campos")
def step_click_login_empty(context):
    context.login_page.click_login_without_credentials()


@then("devo ser redirecionado para a página de inventário")
def step_check_inventory_redirect(context):
    assert context.login_page.is_login_successful(), (
        f"Login não foi bem-sucedido. URL atual: {context.driver.current_url}"
    )


@then('devo ver a mensagem de erro "{mensagem}"')
def step_check_error_message(context, mensagem):
    actual = context.login_page.get_error_message()
    assert actual == mensagem, (
        f"Mensagem incorreta.\n  Esperado : '{mensagem}'\n  Obtido   : '{actual}'"
    )
