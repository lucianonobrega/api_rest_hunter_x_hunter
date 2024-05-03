from flask import Flask, jsonify, request
import mysql.connector

class ApiRest():
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="apirest"
            )
            self.cursor = self.mydb.cursor()
            self.app = Flask(__name__)
            self.app.json.sort_keys = False
        except mysql.connector.Error as E:
            print(f"Aconteu um erro: {E}.")

    def buscar_personagens(self):
        try:
            comando = "SELECT * FROM hunter_db"
            self.cursor.execute(comando)
            personagens = self.cursor.fetchall()
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
        except mysql.connector.Error as E:
            return f"Aconteceu um erro: {E}"

    def rota_personagens_get(self):
        @self.app.route("/personagens", methods=["GET"])
        def personagens():
            lista_personagens = self.buscar_personagens()
            return jsonify(
                mensagem="Lista de personagens",
                dados=lista_personagens
            )

    def rota_personagensid_get(self):
        @self.app.route("/personagens/<int:id>", methods=["GET"])
        def personagem(id):
            lista_personagens = self.buscar_personagens()
            for personagem in lista_personagens:
                if personagem.get("id") == id:
                    return jsonify(
                        mensagem="Personagem:",
                        personagem=personagem)
            return "ID inexistente."

    def rota_personagens_post(self):
        @self.app.route("/personagens", methods=["POST"])
        def adicionar_personagem():
            try:
                novo_personagem = request.get_json()
                comando = "INSERT INTO hunter_db (nome,idade,sexo,altura,peso,aniversario,nen) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s)"
                dados = (novo_personagem['nome'],
                         novo_personagem['idade'],
                         novo_personagem['sexo'],
                         novo_personagem['altura'],
                         novo_personagem['peso'],
                         novo_personagem['aniversário'],
                         novo_personagem['nen'])
                self.cursor.execute(comando,dados)
                self.mydb.commit()
                return jsonify(mensagem="Personagem cadastrado com sucesso!")
            except mysql.connector.Error as E:
                return f"Aconteceu um erro: {E}"

    def rota_personagensid_put(self):
        @self.app.route("/personagens/<int:id>", methods=["PUT"])
        def editar_personagem(id):
            try:
                personagem_alterado = request.get_json()
                comando = "UPDATE hunter_db SET nome = %s," \
                          "idade = %s, sexo = %s, altura = %s," \
                          "peso = %s, aniversario = %s, nen = %s" \
                          "WHERE ID = %s"
                dados = (personagem_alterado['nome'],personagem_alterado['idade'],
                         personagem_alterado['sexo'],personagem_alterado['altura'],
                         personagem_alterado['peso'],personagem_alterado['aniversário'],
                         personagem_alterado['nen'], id)
                self.cursor.execute(comando,dados)
                self.mydb.commit()
                return jsonify(mensagem="Personagem atualizado com sucesso!")
            except mysql.connector.Error as E:
                return f"Aconteceu um erro: {E}"

    def rota_personagensid_delete(self):
        @self.app.route("/personagens/<int:id>", methods=["DELETE"])
        def deletar_personagem(id):
            try:
                comando = "DELETE FROM hunter_db WHERE ID = %s"
                dados = (id,)
                self.cursor.execute(comando,dados)
                self.mydb.commit()
                return jsonify(
                    mensagem="Personagem deletado com sucesso!"
                )
            except mysql.connector.Error as E:
                return f"Aconteceu um erro: {E}"

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    api = ApiRest()
    api.rota_personagens_get()
    api.rota_personagensid_get()
    api.rota_personagens_post()
    api.rota_personagensid_put()
    api.rota_personagensid_delete()
    api.run()