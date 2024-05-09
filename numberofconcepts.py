def calcular_conceito(nota):
    if nota >= 9 and nota <= 10:
        return 'A'
    elif nota >= 8 and nota < 9:
        return 'B'
    elif nota >= 7 and nota < 8:
        return 'C'
    elif nota >= 5 and nota < 7:
        return 'D'
    else:
        return 'F'
def main():
    n = int(input())
    notas = []
    for i in range(n):
        nota = float(input())
        notas.append(nota)
    conceitos = [calcular_conceito(nota) for nota in notas]
    media = sum(notas) / n
    conceitos_contagem = {conceito: conceitos.count(conceito) for conceito in set(conceitos)}
    ordem_conceitos = ['A', 'B', 'C', 'D', 'F']
    for conceito in ordem_conceitos:
        quantidade = conceitos_contagem.get(conceito, 0)
        print(f"{conceito}: {quantidade}")
    print(f"Media: {media:.2f}")
main()