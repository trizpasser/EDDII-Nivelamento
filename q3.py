string = 'teste'
stringFinal = []
pilha = []
i = 0

while i < len(string):
    pilha.append(string[i])
    i += 1

for j in string:
    stringFinal += pilha.pop()

print(stringFinal)
