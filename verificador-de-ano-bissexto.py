def verificar_ano_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

def main():
    try:
        ano = int(input("Digite o ano para verificar se é bissexto: "))
        if ano < 0:
            print("Por favor, insira um ano válido (número positivo).")
            return

        if verificar_ano_bissexto(ano):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Por favor, digite um número inteiro válido para o ano.")

if __name__ == "__main__":
    main()
