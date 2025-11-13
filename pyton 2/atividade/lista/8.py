respostas_alunos = ["A","C","B","D","A"]
gabarito = ["A","D","B","D","C"]
acerto = 0

for i in (range(len(respostas_alunos))):
    if respostas_alunos[i] == gabarito[i]:
        acerto = acerto + 1
print(acerto)
