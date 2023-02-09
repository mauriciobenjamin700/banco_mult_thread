from datetime import datetime

#este pacote visa retornar a data e hora de forma formatada em pt br

def data_hora():
    data = str(datetime.now())

    ano = data[0:4]
    mes = data[5:7]
    dia = data[10:13]


    data_formatada = f'{dia}/{mes}/{ano}'


    hora = data[11:16]
    #seria ideal retornar uma tupla
    return f'{data_formatada} as {hora}'

def data():
    data = str(datetime.now())
    ano = data[0:4]
    mes = data[5:7]
    dia = data[8:10]


    data_formatada = f'{dia}/{mes}/{ano}'

    return data_formatada

def hora():
    data = str(datetime.now())
    hora = data[11:16]

    return hora