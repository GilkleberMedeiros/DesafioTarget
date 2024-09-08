text = input("Digite um texto qualquer: ")

a_count = 0
for c in text.lower():
    if c == "a":
        a_count += 1

if a_count:
    print(f"A letra 'a' aparece {a_count} vezes no texto recebido!")
else:
    print("A letra 'a' não aparece no texto recebido!")