MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade:   "))

if idade >= MAIOR_IDADE: 
    print("Você tem mais de 18, você pode tirar a CNH")

if idade <= MAIOR_IDADE: 
    print("Você ainda é menor de idade, não pode tirar a CNH")

if idade >= MAIOR_IDADE: 
    print("Você tem mais de 18, você pode tirar a CNH")
else: 
    print("Você ainda é menor de idade, não pode tirar a CNH")
    

if idade >= MAIOR_IDADE: 
    print("Você tem mais de 18, você pode tirar a CNH")
elif idade >= IDADE_ESPECIAL: 
    print("VOcê não é maior de idade, mas pode fazer as aulas teroricas, mas não pode fazer as aulas praticas")
else: 
    print("Você não pode fazer nenhum tipo de aula")