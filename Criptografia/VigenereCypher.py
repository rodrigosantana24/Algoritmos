def gerar_chave(mensagem, chave):
    chave = list(chave)
    if len(mensagem) == len(chave):
        return "".join(chave)
    else:
        for i in range(len(mensagem) - len(chave)):
            chave.append(chave[i % len(chave)])
    return "".join(chave)


def cifra_vigenere(mensagem, chave):
    mensagem = mensagem.upper().replace(" ", "")
    chave = gerar_chave(mensagem, chave.upper())
    cifra = []

    for m, k in zip(mensagem, chave):
        letra = (ord(m) - 65 + ord(k) - 65) % 26
        cifra.append(chr(letra + 65))
    return "".join(cifra)


def decifra_vigenere(cifra, chave):
    cifra = cifra.upper().replace(" ", "")
    chave = gerar_chave(cifra, chave.upper())
    mensagem = []

    for c, k in zip(cifra, chave):
        letra = (ord(c) - 65 - (ord(k) - 65)) % 26
        mensagem.append(chr(letra + 65))
    return "".join(mensagem)

if __name__=="__main__":
    mensagem = "ATAQUEAMANHA"
    chave = "LIMAO"

    cifrado = cifra_vigenere(mensagem, chave)
    decifrado = decifra_vigenere(cifrado, chave)

    print("Mensagem original :", mensagem)
    print("Chave             :", chave)
    print("Mensagem cifrada  :", cifrado)
    print("Mensagem decifrada:", decifrado)
