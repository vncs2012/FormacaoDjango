def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica Destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e Destino não pode ser iguais'


def campo_tem_algum_numero(valor, campo, lista_de_erros):
    """Verifica se possue algum digito numero"""
    if any(char.isdigit() for char in valor):
        lista_de_erros[campo] = 'Não inclua numero neste campo'


def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se data ida e maior que data de volta"""
    if(data_ida > data_volta):
        lista_de_erros['data_volta'] = 'Data de Volta nao pode ser menor que data de Ida'


def data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se data ida menor que data de hoje"""
    if(data_ida < data_pesquisa):
        lista_de_erros['data_ida'] = 'Data de ida não pode menor que hoje'
