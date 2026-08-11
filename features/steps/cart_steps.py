from behave import given, when, then
from pages.home_page import HomePage
from pages.cart_page import CartPage


@given("adicionei um produto ao carrinho")
def step_add_product_to_cart(context):
    context.home_page = HomePage(context.driver)
    context.home_page.add_first_item_to_cart()


@when("vou para o carrinho")
def step_go_to_cart(context):
    if not hasattr(context, "home_page"):
        context.home_page = HomePage(context.driver)
    context.home_page.go_to_cart()
    context.cart_page = CartPage(context.driver)


@given("fui para o carrinho")
def step_went_to_cart(context):
    step_go_to_cart(context)


@then("o carrinho deve conter ao menos 1 item")
def step_cart_has_items(context):
    assert not context.cart_page.is_empty(), "O carrinho deveria conter itens."


@when("removo o primeiro item")
def step_remove_first_item(context):
    context.cart_page.remove_first_item()


@then("o carrinho deve estar vazio")
def step_cart_is_empty(context):
    assert context.cart_page.is_empty(), "O carrinho deveria estar vazio após a remoção."


@when("clico em Continuar Comprando")
def step_continue_shopping(context):
    context.cart_page.continue_shopping()


@then("devo estar na página de inventário")
def step_on_inventory_page(context):
    assert "/inventory.html" in context.driver.current_url, (
        f"URL esperada conter '/inventory.html', atual: {context.driver.current_url}"
    )
