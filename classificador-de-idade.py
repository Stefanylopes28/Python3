def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida."
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

def main():
    try:
        idade = int(input("Digite a sua idade: "))
        classificacao = classificar_idade(idade)
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira um número inteiro válido para a idade.")

if __name__ == "__main__":
    main()
