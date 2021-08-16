import csv
import pickle
import json

from contato import Contato


def csv_para_contatos(path, encoding="latin_1"):
    contatos = []

    with open(path, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos


def contatos_para_pickle(contatos, path):
    with open(path, mode="wb") as arquivo:
        pickle.dump(contatos, arquivo)


def pickle_para_contatos(path):
    with open(path, mode="rb") as arquivo:
        contatos = pickle.load(arquivo)

    return contatos


def converter_json(contatos, path):
    with open(path, mode="w") as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)


def _contato_para_json(contato):
    return contato.__dict__


def json_para_contatos(path):
    contatos = []

    with open(path) as arquivo:
        contatos_json = json.load(arquivo)
        for contato in contatos_json:
            c = Contato(**contato)
            contatos.append(c)

    return contatos
