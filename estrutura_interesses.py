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


def todas_as_pessoas():
    return database['PESSOAS']


def localiza_pessoa(id_pessoa): 
    raise NotFoundError


def adiciona_pessoa(dic_pessoa):
    database['PESSOAS'].append(dic_pessoa)
    database['INTERESSES'][dic_pessoa['id']] = []
                                     

def adiciona_interesse(id_interessado, id_alvo_de_interesse):
    if not database['PESSOAS'].get(id_interessado):
        raise NotFoundError(f"Não foi possível encontrar a pessoa com id {id_interessado}")
    if not database['PESSOAS'].get(id_alvo_de_interesse):
        raise NotFoundError(f"Não foi possível encontrar a pessoa com id {id_alvo_de_interesse}")
        
    if id_alvo_de_interesse in database['INTERESSES'].get(id_interessado, []):
        return
        
    database['INTERESSES'][id_interessado].append(id_alvo_de_interesse)


def consulta_interesses(id_interessado):
    try:
        pessoa = [p for p in database['PESSOAS'] if p['id'] == id_interessado][0]
    except IndexError:
        raise NotFoundError('Pessoa não encontrada na lista')
    
    lista_interesses = []
    for interesse in database['INTERESSES']:
        if interesse == id_interessado:
            lista_interesses.extend(database['INTERESSES'][interesse])
    
    return lista_interesses


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
