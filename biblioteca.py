from flask import Flask, jsonify, request
from model.database import Biblioteca
from service.service import validar_data, validar_campos, validar_valores_negativos

DB = Biblioteca()
app = Flask(__name__)

#Endpoint GET para testar, se API está ligada
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'Api conectada'}), 200

#Endpoint POST para cadastrar um novo livro no banco
@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    dados = request.get_json()
    
    if not dados:
        return jsonify({'msg': 'Requisição inválida'}), 400
    
    nome = dados.get('nome')
    autor = dados.get('autor')
    preco = dados.get('preco')
    ano = dados.get('ano')
    data_retirada = dados.get('data_retirada')
    data_entrega = dados.get('data_entrega')

    if not validar_campos(nome,autor,preco,ano,data_retirada,data_entrega):
        return jsonify({"msg": "Não deixe campos vazios !"}), 400
    if validar_data(data_retirada,data_entrega) is False:
        return jsonify({"msg": 'A data estão inválidas !'}), 400
    if validar_valores_negativos(preco):
        return jsonify({'msg': 'Valores negativos não são validos !'}), 400
    

    cadastrou = DB.cadastrar_livro(nome,autor,preco,ano,data_retirada,data_entrega)
    if cadastrou:
        return jsonify({'msg': 'Livro cadastrado com sucesso !'}), 201
    return jsonify({'msg': 'Erro ao cadastrar livro'}), 500

#Endpoint GET para listar todos os livros cadastrados
@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = DB.listar_livros()
    if not livros:
        return jsonify({'msg': 'Nenhum livro cadastrado'}), 404
    return jsonify({"livros": livros}), 200

#Endpoint DELETE para deletar um livro pelo ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    deletou = DB.excluir_livro(id)
    if deletou:
        return jsonify({'msg': 'Livro excluido com sucesso'}), 200
    return jsonify({'msg': 'Livro não encontrado'}), 404

#Endpoint GET para buscar apenas um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    livro = DB.buscar_livro(id)

    if not livro:
        return jsonify({'msg': 'Livro não encontrado'}), 404
    return jsonify({"livro": livro}), 200

if __name__ == "__main__":
    app.run(debug=True)