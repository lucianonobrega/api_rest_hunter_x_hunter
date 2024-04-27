from flask import Flask, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="apirest"
)

cursor = mydb.cursor()

def buscar_personagens():
    comando = "SELECT * FROM hunter_db"
    cursor.execute(comando)
    personagens = cursor.fetchall()
    lista_personagens = list()
    for personagem in personagens:
        lista_personagens.append(
            {
                "id": personagem[0],
                "nome": personagem[1],
                "idade": personagem[2],
                "sexo": personagem[3],
                "altura": personagem[4],
                "peso": personagem[5],
                "aniversário": personagem[6],
                "nen": personagem[7]
            }
        )
    return lista_personagens

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/personagens", methods=["GET"])
def personagens():
    lista_personagens = buscar_personagens()
    return jsonify(
        mensagem="Lista de personagens",
        dados=lista_personagens
    )

@app.route("/personagens/<int:id>", methods=["GET"])
def personagem(id):
    lista_personagens = buscar_personagens()
    for personagem in lista_personagens:
        if personagem.get("id") == id:
            return jsonify(
                mensagem="Personagem:",
                personagem=personagem)
    return "ID inexistente."

@app.route("/personagens", methods=["POST"])
def adicionar_personagem():
    novo_personagem = request.get_json()
    comando = f"INSERT INTO hunter_db (nome,idade,sexo,altura,peso,aniversario,nen) " \
              f"VALUES ('{novo_personagem['personagem']['nome']}'," \
              f"'{novo_personagem['personagem']['idade']}'," \
              f"'{novo_personagem['personagem']['sexo']}'," \
              f"'{novo_personagem['personagem']['altura']}'," \
              f"'{novo_personagem['personagem']['peso']}'," \
              f"'{novo_personagem['personagem']['aniversário']}'," \
              f"'{novo_personagem['personagem']['nen']}')"
    cursor.execute(comando)
    mydb.commit()
    return jsonify(mensagem="Personagem cadastrado com sucesso!")

@app.route("/personagens/<int:id>", methods=["PUT"])
def editar_personagem(id):
    personagem_alterado = request.get_json()
    comando = f"UPDATE hunter_db SET nome='{personagem_alterado['personagem']['nome']}'," \
              f"idade='{personagem_alterado['personagem']['idade']}'," \
              f"sexo='{personagem_alterado['personagem']['sexo']}'," \
              f"altura='{personagem_alterado['personagem']['altura']}'," \
              f"peso='{personagem_alterado['personagem']['peso']}'," \
              f"aniversario='{personagem_alterado['personagem']['aniversário']}'," \
              f"nen='{personagem_alterado['personagem']['nen']}'" \
              f"WHERE ID = {id}"
    cursor.execute(comando)
    mydb.commit()
    return jsonify(mensagem="Personagem atualizado com sucesso!")

@app.route("/personagens/<int:id>", methods=["DELETE"])
def deletar_personagem(id):
    comando = f"DELETE FROM hunter_db WHERE ID = {id}"
    cursor.execute(comando)
    mydb.commit()
    return jsonify(
        mensagem="Personagem deletado com sucesso!"
    )

if __name__ == "__main__":
    app.run(debug=True)