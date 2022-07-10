def start_menu():
    menu_items = ['1', '2', '3', '0']
    menu_message = """
        Bem vindo(a)!
        Escolha uma acao:

        [1] Gerenciar Serie
        [2] Gerenciar Medias Moveis
        [3] Gerar Saida

        [0] Sair do Programa
        """
    print(menu_message)
    ask_for_choose()
    return menu_items


def price_menu():
    menu_items = ['1', '2', '3', '0']
    menu_message = """
        [1] Adicionar itens
        [2] Mostrar Serie atual 
        [3] Excluir item

        [0] Voltar para Menu 
    """
    print(menu_message)
    ask_for_choose()
    return menu_items


def average_menu():
    menu_items = ['1', '2', '0']
    menu_message = """
        Escolha uma media para detetminar:

        [1] Media Movel Curta
        [2] Media Movel Longa

        [0] Voltar para Menu
    """
    print(menu_message)
    return menu_items


def ask_for_choose():
    choose = "Digite o numero da opcao desejada: "
    print(choose)


def short_average():
    short_average = "Digite o valor da Media Movel Curta: "
    print(short_average)


def long_average():
    long_average = "Digite o valor da Media Movel Longa: "
    print(long_average)
