database = {}

class NotFoundError(Exception):
    pass

database['PESSOAS'] = [
    {"id": 9, "nome": "Marcos"}, 
    {"id": 3, "nome": "Ana"}, 
    {'nome':'Fernando','id':1},
    {'nome':'Olga','id':10}
]

database['INTERESSES'] = { 
    9: [3,10], 
    1: [3],
    3: [9],
    10: [9,1]
}

def reseta():
    database["PESSOAS"] = []
    database['INTERESSES'] = {}


def criar_perfil(nome, idade, genero, interesses):
    perfil = {
        "nome": nome,
        "idade": idade,
        "genero": genero,
        "interesses": interesses
    }
    return perfil


def combinar_interesses(interesses1, interesses2):
    interesses_combinados = interesses1 + interesses2
    interesses_combinados.sort()
    return interesses_combinados


def todas_as_pessoas():
    return database['PESSOAS']

def localiza_pessoa(id_pessoa):
    for pessoa in database['PESSOAS']:
        if pessoa['id'] == id_pessoa:
            return pessoa
    
    raise NotFoundError(f"Pessoa com id {id_pessoa} não encontrada")


def adiciona_pessoa(dic_pessoa):
    database['PESSOAS'].append(dic_pessoa)
    database['INTERESSES'][dic_pessoa.get('id', None)] = []
                                     

def adiciona_interesse(id_interessado, id_alvo_de_interesse):
    if not any(p['id'] == id_interessado for p in database['PESSOAS']):
        raise NotFoundError(f"Não foi possível encontrar a pessoa com id {id_interessado}")
    if not any(p['id'] == id_alvo_de_interesse for p in database['PESSOAS']):
        raise NotFoundError(f"Não foi possível encontrar a pessoa com id {id_alvo_de_interesse}")
        
    interesses = database['INTERESSES'].get(id_interessado, [])
    if id_alvo_de_interesse not in interesses:
        interesses.append(id_alvo_de_interesse)
        database['INTERESSES'][id_interessado] = interesses

def consulta_interesses(id_interessado):
    try:
        interesses = database['INTERESSES'][id_interessado]
    except KeyError:
        raise NotFoundError(f"Pessoa com id {id_interessado} não encontrada")
    
    return interesses
    



def remove_interesse(id_interessado, id_alvo_de_interesse):
    if id_interessado not in [p['id'] for p in database['PESSOAS']]:
        raise ValueError("Pessoa com ID {} não existe na lista de pessoas.".format(id_interessado))

    if id_alvo_de_interesse not in [p['id'] for p in database['PESSOAS']]:
        raise ValueError("Pessoa com ID {} não existe na lista de pessoas.".format(id_alvo_de_interesse))

    if id_alvo_de_interesse not in database['INTERESSES'].get(id_interessado, []):
        raise ValueError("Não existe interesse entre a pessoa {} e a pessoa {}.".format(id_interessado, id_alvo_de_interesse))

    database['INTERESSES'][id_interessado].remove(id_alvo_de_interesse)


def lista_matches(id_pessoa):
    try:
        interesses = database['INTERESSES'][id_pessoa]
    except KeyError:
        raise NotFoundError(f"Pessoa com id {id_pessoa} não existe")

    matches = []
    for interesse in interesses:
        try:
            interessados = database['INTERESSES'][interesse]
        except KeyError:
            continue
        
        if id_pessoa in interessados:
            matches.append(interesse)
    
    return matches
