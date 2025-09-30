notas = []
media = -1
situacao = "nao calculado."

while True:
    print(10*"=" + " MENU " + 10*"=")
    print (
        "[0] encerrar o programa\n"
        "[1] adicionar notas\n"
        "[2] calcular situacao do aluno\n"
        "[3] gerar relatorio final"
        )
    code = input("> ")

    # encerrando o programa
    if code == '0':
        print("finalizando programa")
        break
    
  # insercao de notas na lista
    elif code == '1':
        for i in range(3):
            user_input = input(f"Digite a {i + 1}° nota:\n> ")

            # se o input for numerico
            if user_input.isnumeric():
                # adiciona input a nota e soma media
                notas.insert(i, int(user_input))
                media = media + notas[i]
            else:
                print("voce digitou um valor invalido, tente novamente")
                break
        
        # se todos as notas forem validas, calcula a media
        media = media / 3

    # situacao
    elif code == '2':
        # situacao
        if media >= 7:
            situacao = 'aprovado' 
        elif media < 7 and media >= 0:
            situacao = 'reprovado' 
        else:
            print("notas nao inseridas, porfavor insira as notas primeiro.")

        print(situacao)

    # relatorio
    elif code == '3':
        if (len(notas) >= 3):
            print(10*"=" + " RELATORIO " + 10*"=")
            print(
                f"Nota 1: {notas[0]}\n"
                f"Nota 2: {notas[1]}\n"
                f"Nota 3: {notas[2]}\n"
                "------------------------\n"
                f"Media: {media:.2f}\n"
                f"Situacao: {situacao}"
            )
        else:
            print("nenhum relatorio feito, por favor digite as notas e calcule a situacao para gerar um relatorio")

    else:
        print("Selecao invalida, tente novamente!")
