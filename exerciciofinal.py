import re

def le_assinatura():
    '''Lê valores dos traços linguísticos do modelo e devolve uma assinatura para comparação com textos'''
    print("Bem-vindo ao detector automático de COH-PIAH.\n")


    tamMedPalavra = float(input("Entre o tamanho médio de palavra: "))
    typeToken = float(input("Entre a relação Type-Token: "))
    hapaxLegomana = float(input("Entre a Razão Hapax Legomana: "))
    tamMedSentenca = float(input("Entre o tamanho médio de sentença: "))
    comMedSentenca = float(input("Entre a complexidade média da sentença: "))
    tamMedFrase = float(input("Entre o tamanho médio de frase: "))

    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]

def le_textos():
    '''Lê vários textos fornecidos pelo usuário e retorna uma lista de textos'''
    textos = []
    i = 1
    while True:
        texto = input(f"Digite o texto {i} (aperte enter para sair): ")
        if not texto:
            break
        textos.append(texto)
        i += 1
    return textos

def separa_sentencas(texto):
    '''Separa um texto em sentenças usando ponto final, exclamação ou interrogação como delimitadores'''
    if isinstance(texto, str):
        sentencas = re.split(r'[.!?]+', texto)
        if sentencas[-1] == '':
            sentencas.pop()
        return sentencas
    else:
        raise ValueError("A entrada para 'separa_sentencas' deve ser uma string.")

def separa_frases(sentenca):
    '''Separa uma sentença em frases usando vírgula, dois-pontos ou ponto e vírgula como delimitadores'''
    if isinstance(sentenca, str):
        return re.split(r'[,:;]+', sentenca)
    else:
        raise ValueError("A entrada para 'separa_frases' deve ser uma string.")

def separa_palavras(frase):
    '''Separa uma frase em palavras com base em espaços em branco'''
    if isinstance(frase, str):
        return frase.split()
    else:
        raise ValueError("A entrada para 'separa_palavras' deve ser uma string.")

def n_palavras_unicas(lista_palavras):
    '''Conta o número de palavras que aparecem uma única vez em uma lista'''
    freq = {}
    unicas = 0
    
    for palavra in lista_palavras:
        palavra = palavra.lower()
        if palavra in freq:
            freq[palavra] += 1
            if freq[palavra] == 2:
                unicas -= 1
        else:
            freq[palavra] = 1
            unicas += 1
    
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Conta o número de palavras diferentes em uma lista de palavras'''
    freq = {}
    for palavra in lista_palavras:
        palavra = palavra.lower()
        if palavra in freq:
            freq[palavra] += 1
        else:
            freq[palavra] = 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Compara duas assinaturas e calcula a média das diferenças absolutas'''
    somatório = sum(abs(a - b) for a, b in zip(as_a, as_b))
    return somatório / len(as_a)

def calcula_assinatura(texto):
    if not isinstance(texto, str):
        raise ValueError("A entrada para 'calcula_assinatura' deve ser uma string.")

    sentencas = separa_sentencas(texto)
    
    frases = []
    for sentenca in sentencas:
        if isinstance(sentenca, str):
            frases.extend(separa_frases(sentenca))
        else:
            raise ValueError("Todos os elementos em 'frases' devem ser strings.")
    
    palavras = []
    for frase in frases:
        if isinstance(frase, str):
            palavras.extend(separa_palavras(frase))
        else:
            raise ValueError("Todos os elementos em 'palavras' devem ser strings.")

    total_letras = sum(len(palavra) for palavra in palavras)
    num_tot_palavras = len(palavras)
    tamMedPalavra = total_letras / num_tot_palavras
    
    typeToken = n_palavras_diferentes(palavras) / num_tot_palavras
    hapaxLegomana = n_palavras_unicas(palavras) / num_tot_palavras
    
    tamMedSentenca = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)
    comMedSentenca = len(frases) / len(sentencas)
    tamMedFrase = sum(len(frase) for frase in frases) / len(frases)
    
    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]


def avalia_textos(textos, assinatura_main):
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura_main, assinatura) for assinatura in assinaturas]
    
    menor_similaridade = min(similaridades)
    posicao = similaridades.index(menor_similaridade) + 1
    
    return posicao


def main():
    assinatura_main = le_assinatura()
    textos = le_textos()
    resultado = avalia_textos(textos, assinatura_main)
    
    print(f"O autor do texto {resultado} está infectado com COH-PIAH")
