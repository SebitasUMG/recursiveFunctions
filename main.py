def convert_to_binary(num):
    if num == 0:
        return '0'
    elif num < 0:
        return '-' + convert_to_binary(-num)
    else:
        return convert_to_binary(num // 2) + str(num % 2)


def count_digits(num):
    if num == 0:
        return 0
    elif num < 0:
        return count_digits(-num)
    else:
        return 1 + count_digits(num // 10)


def calculate_square_root(num, candidate, approximation):
    if abs(candidate ** 2 - num) < approximation:
        return candidate
    else:
        new_candidate = 0.5 * (candidate + num / candidate)
        return calculate_square_root(num, new_candidate, approximation)


def integer_square_root(num):
    if num < 0:
        raise ValueError("No se puede calcular el valor de un numero negativo.")
    return calculate_square_root(num, 1, 0.00000000000001)


def convert_roman_to_decimal(roman_num):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not roman_num:
        return 0

    if len(roman_num) == 1 or roman_numerals[roman_num[0]] >= roman_numerals[roman_num[1]]:
        return roman_numerals[roman_num[0]] + convert_roman_to_decimal(roman_num[1:])
    else:
        return roman_numerals[roman_num[1]] - roman_numerals[roman_num[0]] + convert_roman_to_decimal(roman_num[2:])


def sum_of_integers(num):
    if num == 0:
        return 0
    elif num < 0:
        raise ValueError("Por favor Ingrese un valor positivo")
    else:
        return num + sum_of_integers(num - 1)


if __name__ == "__main__":
    while True:
        print("\nBienvenidos al programa de conversaciones")
        print("===========================================")
        print("\nEliga una opcion:")
        print("1. Convertir un entero a binario")
        print("2. Contar digitos de un numero")
        print("3. Raiz quadrada entera")
        print("4. Convertir numero romano a decimal")
        print("5. Suma de numeros enteros")
        print("6. Salir")

        option = input("Eliga una opcion a realizar: \n")

        if option == '1':
            number = int(input("Ingrese un numero entero: \n"))
            print(f"Su representacion en binario es: {convert_to_binary(number)}")

        elif option == '2':
            number = int(input("Ingrese un numero entero: \n"))
            print(f"La cantidad de digitos que hay es de: {count_digits(number)}")

        elif option == '3':
            number = float(input("Ingrese un numero entero: \n: "))
            print(f"La raiz cuadrada es de: {integer_square_root(number)}")

        elif option == '4':
            roman = input("Ingrese un numero romano: \n")
            print(f"El numero en decimales es: {convert_roman_to_decimal(roman)}")

        elif option == '5':
            number = int(input("Ingrese un numero entero positivo: "))
            print(f"La suma actual más {number} es: {sum_of_integers(number)}")

        elif option == '6':
            print("Saliendo del programa.....")
            break

        else:
            print("Opcion invalida, por favor ingrese una opcion valida del sistema")
