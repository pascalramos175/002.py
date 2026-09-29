import os

# Estrutura para armazenar os dados cadastrados temporariamente
banco_de_dados = []

def limpar_tela():
    """Limpa o terminal para manter o menu organizado."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_pessoa():
    limpar_tela()
    print("=== CADASTRAR NOVA PESSOA ===")
    
    # Capturando dados através da função input()
    nome = input("Digite o nome completo: ").strip()
    
    # Tratamento de erro simples para garantir que a idade seja um número inteiro
    while True:
        try:
            idade = int(input("Digite a idade: "))
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")
            
    email = input("Digite o e-mail: ").strip()
    telefone = input("Digite o telefone (com DDD): ").strip()
    
    # Criando o dicionário com os dados pessoais
    pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Email": email,
        "Telefone": telefone
    }
    
    banco_de_dados.append(pessoa)
    print(f"\n✅ {nome} foi cadastrado(a) com sucesso!")
    input("\nPressione Enter para voltar ao menu...")

def listar_pessoas():
    limpar_tela()
    print("=== PESSOAS CADASTRADAS ===")
    
    if not banco_de_dados:
        print("Nenhum dado pessoal foi registrado ainda.")
    else:
        for idx, pessoa in enumerate(banco_de_dados, start=1):
            print(f"\n[Registro #{idx}]")
            for chave, valor in pessoa.items():
                print(f"  {chave}: {valor}")
            print("-" * 30)
            
    input("\nPressione Enter para voltar ao menu...")

def menu_principal():
    while True:
        limpar_tela()
        print("=================================")
        print("  SISTEMA DE DADOS PESSOAIS     ")
        print("=================================")
        print("1. Cadastrar nova pessoa")
        print("2. Listar pessoas cadastradas")
        print("3. Sair")
        print("=================================")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Escolha um número entre 1 e 3.")
            input("Pressione Enter para tentar novamente...")

# Inicia o aplicativo executando o menu interativo
if __name__ == "__main__":
    menu_principal()

 
