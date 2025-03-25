from models.banco import Banco

def exibir_menu_principal():
    print("\n=== Sistema Bancário ===")
    print("1. Cadastrar novo cliente")
    print("2. Acessar conta")
    print("3. Sair")
    return input("Escolha uma opção: ")

def exibir_menu_cliente():
    print("\n=== Menu do Cliente ===")
    print("1. Criar nova conta")
    print("2. Realizar depósito")
    print("3. Realizar saque")
    print("4. Realizar transferência")
    print("5. Consultar saldo")
    print("6. Ver histórico")
    print("7. Voltar ao menu principal")
    return input("Escolha uma opção: ")

def cadastrar_cliente(banco: Banco):
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")
    
    if banco.cadastrar_cliente(nome, cpf, senha):
        print("Cliente cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar cliente. CPF já cadastrado.")

def acessar_conta(banco: Banco):
    print("\n=== Acesso à Conta ===")
    cpf = input("CPF: ")
    senha = input("Senha: ")
    
    cliente = banco.autenticar_cliente(cpf, senha)
    if cliente:
        while True:
            opcao = exibir_menu_cliente()
            
            if opcao == "1":
                criar_conta(banco, cliente)
            elif opcao == "2":
                realizar_deposito(banco, cliente)
            elif opcao == "3":
                realizar_saque(banco, cliente)
            elif opcao == "4":
                realizar_transferencia(banco, cliente)
            elif opcao == "5":
                consultar_saldo(cliente)
            elif opcao == "6":
                ver_historico(cliente)
            elif opcao == "7":
                break
            else:
                print("Opção inválida!")
    else:
        print("CPF ou senha inválidos!")

def criar_conta(banco: Banco, cliente: Cliente):
    print("\n=== Criar Nova Conta ===")
    print("1. Conta Corrente")
    print("2. Conta Poupança")
    tipo = input("Escolha o tipo de conta: ")
    
    numero = input("Número da conta: ")
    saldo = float(input("Saldo inicial: "))
    
    if tipo == "1":
        limite = float(input("Limite da conta: "))
        if banco.criar_conta_corrente(cliente.cpf, numero, saldo, limite):
            print("Conta corrente criada com sucesso!")
        else:
            print("Erro ao criar conta.")
    elif tipo == "2":
        taxa_juros = float(input("Taxa de juros (%): "))
        if banco.criar_conta_poupanca(cliente.cpf, numero, saldo, taxa_juros):
            print("Conta poupança criada com sucesso!")
        else:
            print("Erro ao criar conta.")
    else:
        print("Tipo de conta inválido!")

def realizar_deposito(banco: Banco, cliente: Cliente):
    print("\n=== Realizar Depósito ===")
    numero = input("Número da conta: ")
    conta = banco.buscar_conta(numero)
    
    if conta and conta.titular == cliente.nome:
        valor = float(input("Valor do depósito: "))
        if conta.depositar(valor):
            print("Depósito realizado com sucesso!")
        else:
            print("Erro ao realizar depósito.")
    else:
        print("Conta não encontrada ou não pertence ao cliente.")

def realizar_saque(banco: Banco, cliente: Cliente):
    print("\n=== Realizar Saque ===")
    numero = input("Número da conta: ")
    conta = banco.buscar_conta(numero)
    
    if conta and conta.titular == cliente.nome:
        valor = float(input("Valor do saque: "))
        if conta.sacar(valor):
            print("Saque realizado com sucesso!")
        else:
            print("Erro ao realizar saque. Saldo insuficiente.")
    else:
        print("Conta não encontrada ou não pertence ao cliente.")

def realizar_transferencia(banco: Banco, cliente: Cliente):
    print("\n=== Realizar Transferência ===")
    numero_origem = input("Número da conta de origem: ")
    numero_destino = input("Número da conta de destino: ")
    valor = float(input("Valor da transferência: "))
    
    conta_origem = banco.buscar_conta(numero_origem)
    conta_destino = banco.buscar_conta(numero_destino)
    
    if conta_origem and conta_origem.titular == cliente.nome and conta_destino:
        if conta_origem.transferir(conta_destino, valor):
            print("Transferência realizada com sucesso!")
        else:
            print("Erro ao realizar transferência. Saldo insuficiente.")
    else:
        print("Conta não encontrada ou não pertence ao cliente.")

def consultar_saldo(cliente: Cliente):
    print("\n=== Consulta de Saldo ===")
    for conta in cliente.contas:
        print(f"Conta {conta.numero}: R$ {conta.saldo:.2f}")

def ver_historico(cliente: Cliente):
    print("\n=== Histórico de Operações ===")
    for conta in cliente.contas:
        print(f"\nConta {conta.numero}:")
        for operacao in conta.historico:
            print(f"Data: {operacao['data']}")
            print(f"Tipo: {operacao['tipo']}")
            print(f"Valor: R$ {operacao['valor']:.2f}")
            print(f"Saldo: R$ {operacao['saldo']:.2f}")
            print("-" * 30)

def main():
    banco = Banco()
    
    while True:
        opcao = exibir_menu_principal()
        
        if opcao == "1":
            cadastrar_cliente(banco)
        elif opcao == "2":
            acessar_conta(banco)
        elif opcao == "3":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 