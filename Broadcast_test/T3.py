#!/usr/bin/env python3

#
# IMPLEMENTAÇÃO DO BROADCAST
# ASDPC
# Prof. Luiz Lima Jr.
#

import pika
import sys
from enum import Enum

Estados = Enum('Estados', 'ESPERANDO LIDER COMANDADO')

idx = None
Nx = []
entrada = None
estado = Estados.OCIOSO
lider = None


canal = None

# EVENTOS

def espontaneamente(msg):
    print('Inciando')
    global lider
    lider = idx
    muda_estado(Estados.LIDERADO)
    envia(idx, Nx[:1])

def recebendo(msg, remetente):
    global lider
    print(f"{idx}: mensagem {msg} recebida de {remetente}")
    if estado == Estados.OCIOSO:
        muda_estado(Estados.LIDERADO)
        lider = idx if idx > msg else msg
        aux = Nx.copy()
        aux.remove(remetente)
        envia(lider, aux)
    elif estado == Estados.LIDERADO:
        if msg == idx:
            print(f"{idx}: Voce agora é o líder")
            muda_estado(Estados.LIDER)
        else:
            lider = idx if idx > msg else msg
            aux = Nx.copy()
            aux.remove(remetente)
            envia(lider,aux)


def quando():
    print("Alarme")

# AÇÕES

def muda_estado(novo_estado):
    global estado
    estado = novo_estado

def envia(msg, destinatario):
    # ORIGEM:MSG
    m = f"{idx}:{msg}"
    for d in destinatario:
        print(f"Enviando {msg} para {d}")
        canal.basic_publish(exchange='', routing_key=d, body=m)

def alarme(p):
    pass


# callback

def callback(ch, method, props, body):
    msg = body.decode().split(':') # ORIGEM:MSG  => ['ORIGEM', 'MSG' ]
    if len(msg) < 2:
        print("Formato de mensagem com erro.")
        return
    origem = msg[0]
    m = msg[1]
    if origem.upper() == "NULL":
        espontaneamente(m)
    else:
        recebendo(m, origem)


def main(meu_id, meus_vizinhos):
    global canal
    conexao = pika.BlockingConnection()     # conecta com broker
    canal = conexao.channel()               # canal para operações

    global idx, Nx

    idx = meu_id
    Nx = meus_vizinhos

    # cria fila
    canal.queue_declare(queue=idx, auto_delete=True)
    for v in Nx:
        canal.queue_declare(queue=v, auto_delete=True)

    canal.basic_consume(queue=idx,
        on_message_callback=callback,
        auto_ack=True)

    try:
        print(f'{idx}: aguardando mensagens')
        canal.start_consuming()
    except KeyboardInterrupt:
        canal.stop_consuming()

    conexao.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"USO: {sys.argv[0]} idx v1 v2 v3 ...")
        exit(1) # erro

    main(sys.argv[1], sys.argv[2:])