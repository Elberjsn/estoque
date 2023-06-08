from banco_loja import *

def buscar_cbx():
    conectar = create_conecction()
    q="SELECT SKU, NAME_PROD FROM PRODUTOS"
    busca = read_query(conectar, q)
    lista_cbx = []
    for b in busca:
        lista_cbx.append(f'{b[0]} - {b[1]}')
    return lista_cbx

def busca_prod():
    conectar =  create_conecction()
    q = 'SELECT * FROM PRODUTOS'
    return read_query(conectar, q)
    
def add_entrada(entradas):
    conectar = create_conecction()
    sku = entradas[0].split('-')[0]

    nf= entradas[1]
    qtd= entradas[1]
    qtd = read_query(conectar, "SELECT QUANTIDADE FROM PRODUTOS WHERE SKU = '{sku}'")[0]
    q=f'UPDATE PRODUTO SET QUANTIDADE = {qtd},NOTA_FISCAL = {nf} WHERE SKU = {sku}'

def cadastrar_novo(novo):
    print(novo)
    conectar = create_conecction()

def buscar_cods():
    conectar = create_conecction()
    s = "SELECT COUNT(ID_PRODUTO) FROM PRODUTOS"


    