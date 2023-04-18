import random
from fractions import Fraction

# Variável para armazenar número de vitórias de A e permitir outras simulaçoes para padronizar médias e evitar volatilidade de outputs
serie = []


# Loop de número de simulaçoes que farão a média. Quanto maior o número mais preciso o resultado
for loop_de_simulações in range(100):
    # Número de vitórias antes de começar o jogo(como os valores de B não serão computados, não há necessidade de associar a A)
    vitorias = 0

    for i in range(200):  # Número de partidas que serão analizadas. Loop inicia uma nova partida assim que a anterior tiver vencedor
        resultado_A = 1  # Número de pontos iniciais de A
        resultado_B = 0  # Número de pontos iniciais de A

        while abs(resultado_A - resultado_B) < 3:  # abs = valor absoluto |x|. Loop para assim que diferença entre os pontos exceder a 3. Se b estiver ganhando, o módulo da diferença garante que o valor possa ser maior que 3 e terminar a partida

            # Probabilidade de 50% para ambos. Um número entre 0-1 é sorteado.
            if random.random() < 0.5:
                resultado_A += 1       # Caso seja menor do que 0.5, A ganha 1 ponto
            else:
                resultado_B += 1       # Caso maior ou igual a 0.5, B ganha 1 ponto

        if resultado_A > resultado_B:  # Necessário para checar quem é o vencedor. Assim que o Loop se incerra, verifica-se se A tem a liderança dos 3 pontos, somando 1 ao número de vitórias
            vitorias += 1

    # Função ou método que adiciona todas as vezes que A ganhou no loop_de_simulações em uma única série de 200 jogos na list 'serie'. Serie apresenta 200 outputs nesse momento
    serie.append(vitorias)

# Os outputs de vitória são inseridos em uma média aritimética que junto ao arredondamento, acha-se o número inteiro de vitórias que A teria na teoria por sua chance de vencer cada partida
media = round(sum(serie) / 100)

print("A média de vitórias de A é", media)  # Para achar esse número

chance_A_vencer = Fraction(media, 200).limit_denominator(
    max_denominator=6)  # Cálculo da chance de A gnahar o jogo. Fraction possibilita razões racionais que não se dividem, assim como estão as múltiplas escolhas. 'limit_denominator' limita que o numerador seja igual ou menor que 6, igual as respostas possíveis, o que impossibilita que o denominador seja um número alto não compreendido

print("A probabilidade de A ganhar o jogo é", chance_A_vencer)
