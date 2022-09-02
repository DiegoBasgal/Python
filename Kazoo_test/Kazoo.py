# !/usr/bin/env python3
# Kazoo

from kazoo.client import KazooClient
from kazoo.client import NodeExistsError
from threading import Semaphore
import json
import ast

def codificar(valor):
    return json.dumps(valor, indent=2).encode("utf-8")

def decodificar(valor):
    return ast.literal_eval(valor.decode())

def struct(nome, codigo = 1): # 0 - Soltar, 1 - Esperar
    return codificar({"nome": nome, "codigo": codigo})

def get_lider(client, node):
    valor = client.get(node)[0]
    if valor == None:
        return decodificar(struct(""))
    elif valor.decode() == "":
        return decodificar(struct(""))
    return decodificar(valor)

def esperar_lider(valor, client, node, espera):
    print("aguarde")
    codigo = get_lider(client, node)["codigo"]
    while codigo == 1:
        print("", end="")
        codigo = get_lider(client, node)["codigo"]
    tentar_lideranca(valor, client, node, espera)

def lideranca(client, node, espera):
    print("Você é líder")
    try:
        while True:
            print("", end="")
    except KeyboardInterrupt:
        print("\nSair\n")
        espera.release()
        client.set(node, struct("", 0))

def tentar_lideranca(valor, client, node, espera):
    lider = get_lider(client, node)
    if lider["codigo"] == 0:
        zk.set(znode, valor)
        lider = get_lider(client, node)
        if leader["nome"] == decodificar(valor)["nome"]:
            lideranca(client, node, espera)
        else:
            print(f"{lider['nome']} é o(a) líder!")
            esperar_lider(valor, client, node, espera)
    else:
        esperar_lider(valor, client, node, espera)


# Criar cliente:

zk = KazooClient() # localhost: 2181
zk.start()

znode = "/asdpc/KazooDiego"

try:
    zk.create(znode, b"Teste_Diego")
    print(znode, "criado!")
except NodeExistsError:
    print(f"{znode} já existe!")

valor = struct(input("Nome: "), 1)
lider = get_lider(zk, znode)["nome"]
espera = Semaphore(0)

if lider == "":
    zk.set(znode, valor)
    leader = get_lider(zk, znode)["nome"]
    if leader == decodificar(valor)["nome"]:
        lideranca(zk, znode, espera)
    else:
        print(f"{lider} é o(a) líder!")
        esperar_lider(valor, zk, znode, espera)
else:
    print(f"{lider} é o(a) líder")
    esperar_lider(valor, zk, znode, espera)
