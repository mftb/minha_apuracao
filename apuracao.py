import pandas as pd
import requests

response = requests.get(
    "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"
)
json_data = response.json()

candidato = []
partido = []
votos = []
porcentagem = []

for info in json_data["cand"]:
    candidato.append(info["nm"])
    partido.append(info["cc"].split(" ")[0])
    votos.append(info["vap"])
    porcentagem.append(info["pvap"])

df_eleicao = pd.DataFrame(list(zip(candidato, partido, votos, porcentagem)), columns=("Candidato", "Partido", "Votos", "Percentual"))

print(df_eleicao)