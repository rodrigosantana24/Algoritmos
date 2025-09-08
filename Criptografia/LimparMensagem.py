def limpar_mensagem(texto: str) -> str:
    acentos = "áàâãéèêíìîóòôõúùûç"
    sem_acentos = "aaaaeeeiiioooouuuc"
    texto_minusculo = texto.lower()
    resultado = ""
    
    for caractere in texto_minusculo:
        if caractere in acentos:
            posicao = acentos.find(caractere)
            resultado += sem_acentos[posicao]
        elif 'a' <= caractere <= 'z':
            resultado += caractere        
    return resultado

if __name__=="__main__":
    entrada = "Olá, tudo bem com você?"
    saida = limpar_mensagem(entrada)

    print(f"Entrada: {entrada}")
    print(f"Saída:   {saida}")

    entrada2 = "A pontuação (100%) foi excelente!"
    saida2 = limpar_mensagem(entrada2)

    print(f"\nEntrada: {entrada2}")
    print(f"Saída:   {saida2}")