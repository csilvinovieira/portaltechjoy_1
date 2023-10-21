while True:
    nome = input("Digite seu nome completo...:")
    ano = input("Digite seu ano de nascimento(entre 1922 e 2021)...:")
    try:
        ano=int(ano)
        if ano < 1922 or ano > 2021:
            raise ValueError
        break
    except ValueError
        print("Ano inválido.Digite um valor entre 1922 e 2021.")
    ano=2022-ano
    print(f"Olá{nome}, você tem {ano} anos")