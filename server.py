from flask import Flask, jsonify, request 
import estrutura_interesses as i

app = Flask(__name__)              
     
#Esse arquivo é o CONTROLLER                              

# /pessoas, com GET, para pegar a lista de todas as pessoas
@app.route("/pessoas", methods=["GET"])
def pessoas():
    lista = i.todas_as_pessoas()
    return jsonify(lista)

# /pessoas, com POST, receber um dicionário de uma pessoa e colocar na lista
@app.route("/pessoas", methods=["POST"])
def add_pessoa():
    #receber um dicionário através do flask?
    # O usuário me mandou alguma coisa, eu acho que foi um json
    # quero que voce transforme num dicionário pra mim
    dic_usuario_enviou = request.json
    i.adiciona_pessoa(dic_usuario_enviou)
    return jsonify({"status":"ok"})


# /pessoas/id_pessoa, com GET, para localizar no dicionario da pessoa pelo id

# /pessoas/interesse, com POST, **aqui não tem corpo de requisição 
# adiciona_interesse (id_interessado, id_alvo_de_interesse): 

# /pessoas/interesse, com GET, 
# consulta_interesses(id_interessado):

# /pessoas/interesse, com DELETE,  
# remove_interesse(id_interessado, id_alvo_de_interesse)

# /pessoas/matches, com GET, 
# lista_matches(id_pessoa): 
    
# /reseta, com POST, para esvaziar a lista de pessoas
@app.route("/reseta", methods=["POST"])
def reseta():
    i.reseta()
    return jsonify({"status":"ok"})
    
if __name__ == '__main__':         #rodar o servidor
   app.run(host = 'localhost', port = 5002, debug = True)