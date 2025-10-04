premier_terme = int(input("Premier terme de la suite: "))

raison = int(input("Raison de la suite: "))

n = int(input("N: "))

print(f"{n}ième nombre de la suite: ", premier_terme + (n-1) * raison)
