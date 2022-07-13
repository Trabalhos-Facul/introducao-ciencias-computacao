import prints
import output_generator
import validator

input_values = []

short_average = 1
long_average = 1

MAX_INVALID_VALUES = 10


def main():
    global short_average, long_average

    menu_start_valid_options = prints.start_menu()

    for i in range(MAX_INVALID_VALUES):

        option_chosen = input()

        if option_chosen in menu_start_valid_options:

            if option_chosen == menu_start_valid_options[0]:

                menu_price_valid_options = prints.price_menu()

                for _ in range(MAX_INVALID_VALUES):

                    option_chosen = input()

                    if option_chosen in menu_price_valid_options:
                        if option_chosen == menu_price_valid_options[0]:
                            print("Digite o valor do item e pressione a tecla Enter para adicionar um item a serie")
                            print("Ou Digite 'q' e pressione a tecla Enter para sair: ")

                            price = str(input().strip())

                            while price != 'q':
                                if validator.is_float(price):
                                    if input_values:
                                        input_values.insert(0, price)
                                    else:
                                        input_values.append(price)
                                    price = str(input().strip())
                                else:
                                    print("Valor invalido, tente novamente: ")
                                    price = str(input().strip())
                            return main()

                        elif option_chosen == menu_price_valid_options[1]:
                            print(input_values)
                            return main()

                        elif option_chosen == menu_price_valid_options[2]:
                            value_to_delete = input()

                            if validator.is_int(value_to_delete):
                                if 0 <= int(value_to_delete) < len(input_values):
                                    del input_values[int(value_to_delete)]
                                else:
                                    print("Posicao invalida")

                            return main()

                        else:
                            return main()

                    print(f"Valor invalido")

            elif option_chosen == menu_start_valid_options[1]:

                menu_average_valid_options = prints.average_menu()

                for _ in range(MAX_INVALID_VALUES):

                    option_chosen = input()

                    if option_chosen in menu_average_valid_options:
                        if option_chosen == menu_average_valid_options[0]:

                            input_to_short_average =  input("Digite o valor da media curta: ")

                            if validator.is_int(input_to_short_average):
                                short_average = int(input_to_short_average)
                                return main()
                            else:
                                print("Valor para media invalido")
                                return main()

                        elif option_chosen == menu_average_valid_options[1]:
                            input_to_long_average = input("Digite o valor da media longa: ")

                            if validator.is_int(input_to_long_average):
                                long_average = int(input_to_long_average)
                                return main()
                            else:
                                print("Valor para media invalido")
                                return main()
                        else:
                            return main()

                    print(f"Valor invalido")

            elif option_chosen == menu_start_valid_options[2]:

                if input_values:

                    data_values = [float(x) for x in input_values]

                    data_short = output_generator.average_in_period(data_values, short_average)
                    data_long = output_generator.average_in_period(data_values, long_average)

                    difference = output_generator.get_difference_sign(data_short, data_long)

                    trend = output_generator.trend(difference)

                    prints.print_output(data_values, data_short, data_long, trend)

                else:
                    print("Nenhum valor na serie")

                return main()

            else:
                return True

        print(f"Valor invalido")

        last_try = i == MAX_INVALID_VALUES - 1

        if last_try:
            print("Limite maximo de tentativas falhas alcancado")
    return True


if __name__ == "__main__":
    main()
