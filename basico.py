vitorias = 0

for i in range(200):
    resultado_A = 1
    resultado_B = 0

    while abs(resultado_A - resultado_B) < 3:
        if random.random() < 0.5:
            resultado_A += 1
        else:
            resultado_B += 1

    if resultado_A > resultado_B:
        vitorias += 1

chance_A_vencer = Fraction(vitorias, 200).limit_denominator(max_denominator=6)

print("Número de vitórias de A:", vitorias)
print("Chance de A ganhar:", chance_A_vencer)
