conta_normal = True
conta_univesitaria = False
cheque_especial = 450
saldo = 2000
saque = 500


if conta_normal:
    if saldo >= saque: 
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso com cheque especial !")
    else:
        print("Não foi possivel realizar o saque. Saldo insuficienre")
        
elif conta_univesitaria:
    if saldo >= saque:
        print("Sque realizado com sucesso!")
    else:
        print("Saldo insuficiente.")
else: 
    print("Não foi identificado o tipo de conta, entre em contato com seu gerente.")