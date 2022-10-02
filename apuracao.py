import os
import time

import pandas as pd
import requests


DATA_URL = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"


def tse():
    """Puxa os dados do TSE."""
    tentativas = 0
    while tentativas < 5:
        try:
            response = requests.get(DATA_URL)
            return response.json()
        except:
            tentativas += 1
            time.sleep(2**tentativas)

def apuracao(resultados):
    """Formata os dados extraídos."""
    print(f"Apurados: {resultados['psi']}%")

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
    """Exibe no terminal."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        resultados = tse()
        apura = apuracao(resultados)
        print(apura)
        time.sleep(5)


if __name__ == "__main__":
    main()