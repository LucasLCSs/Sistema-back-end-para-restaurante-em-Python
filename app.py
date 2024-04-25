import os

restaurantes = [{'nome':'McDonalds', 'categoria':'Hamburguer','ativo':True},
                {'nome':'Turatti','categoria':'Comidas tradicionais','ativo':False},
                {'nome':'DomLazio','categoria':'Pizzaria','ativo':True}]

def exibir_nome_do_programa():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼​​​​​\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()

def exibi_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Alterar Status do restaurante')
    print('3. Mostrar Lista de restaurantes cadastrados')
    print('4. Sair\n')

def alternar_estado_restaurante():
    print('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado!')
    voltar_ao_menu_principal()

def finalizar_app():
    os.system('cls')
    print('Você saiu, tenha um otimo dia e volte sempre!\n')

def opcao_invalida():
    print('Opção invalida!')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    os.system('cls')
    
    cadastro_restaurante = input('Cadastrar restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {cadastro_restaurante}: ')
    dados_do_restaurante = {'nome':cadastro_restaurante, 'categoria':categoria_restaurante, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {cadastro_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def lista_de_restaurantes():
    print('LISTA DE RESTAURANTES\n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for item in restaurantes:
        nome_restaurante = item['nome']
        categoria_restaurante = item['categoria']
        ativo_restaurante = 'ativo' if item ['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante.ljust(20)}')

    voltar_ao_menu_principal()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            alternar_estado_restaurante
        elif opcao_escolhida == 3:
            lista_de_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibi_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()