from behave import when, then
from pages.home_page import HomePage


@then("devo ver a lista de produtos")
def step_see_product_list(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.is_loaded(), "A lista de produtos não foi carregada."


@then("devo ver {quantidade:d} produtos no inventário")
def step_count_products(context, quantidade):
    context.home_page = HomePage(context.driver)
    actual = context.home_page.get_product_count()
    assert actual == quantidade, f"Esperado {quantidade} produtos, encontrado {actual}."


@when("adiciono o primeiro produto ao carrinho")
def step_add_first_to_cart(context):
    context.home_page = HomePage(context.driver)
    context.home_page.add_first_item_to_cart()


@then('o badge do carrinho deve exibir "{quantidade}"')
def step_check_cart_badge(context, quantidade):
    actual = context.home_page.get_cart_badge_count()
    assert actual == quantidade, (
        f"Badge esperado: '{quantidade}', obtido: '{actual}'"
    )


@when('ordeno os produtos por "{ordenacao}"')
def step_sort_products(context, ordenacao):
    context.home_page = HomePage(context.driver)
    context.home_page.select_sort(ordenacao)


@then('os produtos devem estar ordenados corretamente por "{ordenacao}"')
def step_verify_sort(context, ordenacao):
    home = context.home_page
    if ordenacao in ("az", "za"):
        names    = home.get_product_names()
        expected = sorted(names, reverse=(ordenacao == "za"))
        assert names == expected, (
            f"Ordem incorreta para '{ordenacao}'.\n  Esperado: {expected}\n  Obtido  : {names}"
        )
    else:
        prices   = home.get_product_prices()
        expected = sorted(prices, reverse=(ordenacao == "hilo"))
        assert prices == expected, (
            f"Ordem incorreta para '{ordenacao}'.\n  Esperado: {expected}\n  Obtido  : {prices}"
        )
