import time

import pandas as pd
import requests

DATA_URL = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"

response = requests.get(DATA_URL)
resultados = response.json()

def tse():
    response = requests.get(DATA_URL)
    return response.json()

def apuracao(resultados):
    candidato = []
    partido = []
    votos = []
    porcentagem = []

    for info in resultados["cand"]:
        candidato.append(info["nm"])
        partido.append(info["cc"].split(" ")[0])
        votos.append(info["vap"])
        porcentagem.append(info["pvap"])

    return pd.DataFrame(
        list(zip(candidato, partido, votos, porcentagem)),
        columns=("Candidato", "Partido", "Votos", "Percentual"),
    )


def main():
    while True:
        resultados = tse()
        apuracao = apuracao(resultados)
        print(apuracao)
        time.sleep(30000)


if __name__ == "__main__":
    main()