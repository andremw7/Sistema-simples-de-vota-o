def validar_cpf(cpf):
    """
    Função simples para validar o CPF.
    Considera válido se tiver 11 dígitos numéricos.
    """
    return cpf.isdigit() and len(cpf) == 11


def votar(candidatos):
    votos = {candidato: 0 for candidato in candidatos}
    cpfs_votantes = set()

    while True:
        print("\nDigite o nome do candidato (ou pressione Enter para finalizar):")
        print("Opções: Corinthians, Palmeiras, São Paulo, Santos, Branco")
        nome = input("Candidato: ").strip()

        if nome == "":
            break

        if nome not in candidatos:
            print("Candidato inválido! Tente novamente.")
            continue

        cpf = input("Digite seu CPF (11 dígitos): ").strip()
        if not validar_cpf(cpf):
            print("CPF inválido! Tente novamente.")
            continue

        if cpf in cpfs_votantes:
            print("CPF já utilizado para votar! Voto não registrado.")
            continue

        cpfs_votantes.add(cpf)
        votos[nome] += 1
        print(f"Voto registrado para {nome}!")

    return votos


def exibir_resultados(votos):
    print("\nResultados da Votação:")
    for candidato, voto in votos.items():
        print(f"{candidato}: {voto} votos")

    vencedor = max(votos, key=votos.get)
    print(f"\nVencedor: {vencedor} com {votos[vencedor]} votos!")


candidatos = ["Corinthians", "Palmeiras", "São Paulo", "Santos", "Branco"]
votos = votar(candidatos)
exibir_resultados(votos)
