def menu():
  print("=================")
  print("Escolha uma ação:")
  print("1 => Página 1")
  print("2 => Página 2")
  print("3 => Página 3")
  print("4 => voltar")
  print("=================")

run = True
paginas = []
pilha = []

while run:
  menu()
  op = str(input())
  if op == '1':
    paginas += ['Pg 1']
    pilha += ['Pg 1']
    print(paginas)
  elif(op == '2'):
    paginas += ['Pg 2'] 
    pilha += ['Pg 2']
    print(paginas)
  elif op == '3':
    paginas += ['Pg 3']
    pilha += ['Pg 3']
    print(paginas)  
  elif op == '4':
    if(len(pilha) == 0):
        print("Vazio")
    else:
        paginas += ['Voltar']
        pilha.pop()
    print(paginas)
  else:
    print(paginas)
    run = False