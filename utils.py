def executar_quiz(perguntas):
    pontos = 0
    print("Bem-vindo ao Quiz!\n")

    for pergunta, alternativas in perguntas.items():
        print(pergunta)
        print(alternativas[0])
        print(alternativas[1])
        print(alternativas[2])

        resposta = input("Digite o número da resposta correta: ")

        if resposta == alternativas[3]:
            print("Correto!\n")
            pontos += 1
        else:
            print("Errado!\n")

    print(f"Você fez {pontos} ponto(s) de {len(perguntas)}.")
