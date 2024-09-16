import psycopg

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    # Abrir uma conexão com o PostgreSQL
    with psycopg.connect(
        host="localhost",
        dbname="20242_fatec_ipi_pbdi_theo",
        user="postgres",
        password="123456"
    ) as conexao:
        # Obter um cursor
        with conexao.cursor() as cursor:
            # Executar um comando SELECT
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (usuario.login, usuario.senha)
            )
            # Verificar se há algum resultado
            result = cursor.fetchone()
    # Devolver True ou False conforme o resultado
    return result is not None

def cadastrar(usuario):
    with psycopg.connect(
        host="localhost",
        dbname="20242_fatec_ipi_pbdi_theo",
        user="postgres",
        password="123456"
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)',
                (usuario.login, usuario.senha)
            )
            conexao.commit()

def menu():
    texto = "0-Fechar\n1-Login\n2-Logoff\n3-Cadastro"
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input('Digite seu login: ')
            senha = input('Digite sua senha: ')
            usuario = Usuario(login, senha)
            print('Usuário OK!' if existe(usuario) else 'Usuário NOK!')
        elif op == 2:
            usuario = None
            print('Logoff realizado com sucesso')
        elif op == 3:
            login = input('Digite o login para o novo usuário: ')
            senha = input('Digite a senha para o novo usuário: ')
            novo_usuario = Usuario(login, senha)
            cadastrar(novo_usuario)
            print('Cadastro OK!')
        else:
            print('Cadastro NOK!')
        
        op = int(input(texto))
    else:
        print('Até mais')

def main():
    menu()

main()