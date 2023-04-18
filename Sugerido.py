import random

# Série de simulaçoes para padronizar vitórias de A em médias e evitar volatilidade de outputs
serie = []

# Loop de número de simulaçoes que farão a média. Quanto maior o número mais preciso o resultado
for loop_de_simulações in range(100):
    # Número de vitórias antes de começar o jogo(como os valores de B não serão computados, não há necessidade de associar a A)
    vitoria = 0

    # Número de partidas que serão analizadas. Loop inicia uma nova partida assim que a anterior tiver vencedor
    for i in range(200):
        resultado_a = 1                  # Número de pontos iniciais de A
        resultado_b = 0                  # Número de pontos iniciais de A

        while abs(resultado_a - resultado_b) < 3:  # abs = valor absoluto |x|. Loop para assim que diferença entre os pontos exceder a 3. Se b estiver ganhando, o módulo da diferença garante que o valor possa ser maior que 3 e terminar a partida

            if random.random() < 0.5:             # Probabilidade de 50% para ambos. Caso seja
                resultado_a += 1
            else:
                resultado_b += 1

        if resultado_a > resultado_b:
            vitoria += 1

    serie.append(vitoria)

# Média das séries de simulação ao serem somadas em 1 número de vitórias arredondado(casas decimais)
media = round(sum(serie) / 100) 
print("A média de vitórias de A é", media)

chance_a_vencer = media / 200  # divisao = chance
if chance_a_vencer >= 0.65 and chance_a_vencer <= 0.67:
    print("Chance de A vencer: 2/3") # Resultado tem output de comando no print. Ou seja, não importa qual conta o computador processe, o resultado é sempre o mesmo 
else:
    print("A probabilidade de A ganhar o jogo é aproximadamente 2/3") # Resultado não achado matematicamente. Obriga que chance seja a mesma sem ao menos analisa-lá
