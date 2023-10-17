def diviser_nombres(a, b):
    if b == 0:
        return "Division par zéro n'est pas autorisée."
    return a / b

num1 = 10
num2 = 0

resultat = diviser_nombres(num1, num2)
print(f"Résultat de la division : {resultat}")
