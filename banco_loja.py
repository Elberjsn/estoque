import mysql.connector
from mysql.connector import Error

def create_conecction(host_name='localhost', user_name='root', user_passwd='@Federal2530', db='LOJA'):
    conecction = None
    try:
        conecction = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_passwd,
            database=db
        )
        print(f'Conectado {db}')
    except Error as er:
        print(f'Error {er}')

    return conecction


def execute_query(conecction, query):
    cursor = conecction.cursor()
    try:
        cursor.execute(query)
        conecction.commit()
        print('OK')
        return True
    except Error as er:
        print(f'Erro {er}')
        return False


def read_query(conecction, query):
    cursor = conecction.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as er:
        print(f'Erro {er}')


table_users= """
CREATE TABLE IF NOT EXISTS USERS(
    ID_USER INT AUTO_INCREMENT PRIMARY KEY, 
    NAME_USER VARCHAR(25) NOT NULL,
    PASSWD VARCHAR(128) NOT NULL,
    EMAIL VARCHAR(50) NOT NULL,
    PERMISION INT NOT NULL
    );
"""

table_produtos = """
CREATE TABLE IF NOT EXISTS PRODUTOS(
    ID_PRODUTO INT AUTO_INCREMENT PRIMARY KEY,
    NOTA_FISCAL INT NOT NULL,
    SKU VARCHAR(10) NOT NULL,
    NAME_PROD VARCHAR(50) NOT NULL,
    FORNECEDOR VARCHAR(50) NOT NULL,
    QUANTIDADE INT NOT NULL,
    CUBAGEM DECIMAL NOT NULL,
    TIPO INT NOT NULL,
    DATA_ENTRADA DATE NOT NULL
)
"""

table_estoque = """
CREATE TABLE IF NOT EXISTS ESTOQUE(
    ID_ESTOQUE INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_PROD INT NOT NULL,
    POSICAO VARCHAR(50) NOT NULL,
    QTD_POSICAO INT NOT NULL,
    FOREIGN KEY (ID_PROD) REFERENCES PRODUTOS(ID_PRODUTO)
);
"""

table_saida = """
CREATE TABLE IF NOT EXISTS SAIDA(
    ID_SAIDA INT AUTO_INCREMENT PRIMARY KEY,
    ID_PROD INT NOT NULL,
    SKU VARCHAR(25) NOT NULL,
    QTD INT NOT NULL,
    ID_USER INT NOT NULL,
    DATA_SAIDA DATE NOT NULL,
    FOREIGN KEY (ID_PROD) REFERENCES PRODUTOS(ID_PRODUTO),
    FOREIGN KEY (ID_USER) REFERENCES USERS(ID_USER)
);
"""

table_movi = """
CREATE TABLE IF NOT EXISTS MOVIMENTAR(
    ID_MOVIMENTAR INT AUTO_INCREMENT PRIMARY KEY,
    ID_PRODUTO INT NOT NULL,
    ID_USER INT NOT NULL,
    TIPO INT NOT NULL,
    QTD INT NOT NULL,
    DATA DATE NOT NULL,
    FOREIGN KEY (ID_PRODUTO) REFERENCES PRODUTOS(ID_PRODUTOS)
    FOREIGN KEY (ID_USER) REFERENCES USERS(ID_USER)
)
"""