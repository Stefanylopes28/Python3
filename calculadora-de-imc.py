def calcular_imc(peso, altura):
    if altura <= 0:
        return None, "Altura inválida."
    imc = round(peso / (altura ** 2), 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    return imc, classificacao

def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc, classificacao = calcular_imc(peso, altura)

        if imc is None:
            print(classificacao)  # mensagem de erro
        else:
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    main()
