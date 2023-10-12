import json

# Creazione del dizionario dell'auto
auto = {
    "marca": "Fiat",
    "modello": "Punto Evo",
    "anno_produzione": 2020,
    "potenza_kW": 80
}

# Nome del file JSON in cui memorizzare i dati dell'auto
nome_file = "auto.json"

# Apertura del file in modalità scrittura (w)
with open(nome_file, "w") as file_json:
    # Utilizzo di json.dump() per scrivere il dizionario nel file JSON
    json.dump(auto, file_json)

print(f"I dati dell'auto sono stati memorizzati in '{nome_file}'.")
