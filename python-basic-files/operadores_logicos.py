print(True and True)
print(True and False)
print(False and False)
print(True and True)
print(True and False)
print(False and False)

saldo = 1000
saque = 250 
limite = 200
conta_especial = True

expressao_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao_1)

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_1)
