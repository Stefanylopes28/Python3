def converter_temperatura(valor, unidade_origem, unidade_destino):
    unidade_origem = unidade_origem.lower()
    unidade_destino = unidade_destino.lower()

    # Converte para Celsius como base
    if unidade_origem == "celsius":
        temp_c = valor
    elif unidade_origem == "fahrenheit":
        temp_c = (valor - 32) * 5 / 9
    elif unidade_origem == "kelvin":
        temp_c = valor - 273.15
    else:
        return None, "Unidade de origem inválida."

    # Converte de Celsius para unidade destino
    if unidade_destino == "celsius":
        resultado = temp_c
    elif unidade_destino == "fahrenheit":
        resultado = (temp_c * 9 / 5) + 32
    elif unidade_destino == "kelvin":
        resultado = temp_c + 273.15
    else:
        return None, "Unidade de destino inválida."

    return round(resultado, 2), None

def main():
    print("Conversor de Temperatura")
    try:
        valor = float(input("Digite a temperatura: "))
        unidade_origem = input("Unidade de origem (Celsius, Fahrenheit, Kelvin): ").strip()
        unidade_destino = input("Unidade de destino (Celsius, Fahrenheit, Kelvin): ").strip()

        resultado, erro = converter_temperatura(valor, unidade_origem, unidade_destino)

        if erro:
            print(f"Erro: {erro}")
        else:
            print(f"{valor} {unidade_origem.capitalize()} equivalem a {resultado} {unidade_destino.capitalize()}.")
    except ValueError:
        print("Por favor, insira um valor numérico válido para a temperatura.")

if __name__ == "__main__":
    main()
