from datetime import datetime


def validar_data(data_r, data_e):
    try:
        data_r = datetime.strptime(data_r, "%d/%m/%Y")
        data_e = datetime.strptime(data_e, "%d/%m/%Y")

        if data_e < data_r:
            return False
    except ValueError:
        return False

def validar_campos(nome, autor, preco, ano, data_retirada, data_entrega):
    campos = [
            nome,
            autor,
            preco,
            ano,
            data_retirada,
            data_entrega
        ]
    return all(campo for campo in campos)
    
def validar_valores_negativos(preco):
        if preco is not None and preco <= 0:
            return False
