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


def actual_series(serie):
    print("Serie atual: ")
    for i, s in enumerate(serie):
        print(f"Posicao {i} - {s}")


def print_output(data_values, data_short, data_long, trend):
    print("  Cotacao      MM Curta    MM Longa    Tendencia")
    for i in range(len(data_values)-1, -1, -1):
        if data_short[i]:
            short_print = f'{data_short[i]:.4f}'
        else:
            short_print = '------'

        if data_long[i]:
            long_print = f'{data_long[i]:.4f}'
        else:
            long_print = '------'

        if i < len(trend):
            if trend[i]:
                trend_print = trend[i]
            else:
                trend_print = '------'
        else:
            trend_print = '------'

        print(f"   {data_values[i]:.4f}      {short_print}      {long_print}      {trend_print}")