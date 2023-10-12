import json

# Creiamo una lista vuota per memorizzare i dati delle automobili
lista_auto = []

# Richiediamo all'utente quanti dati di automobili vuole inserire
nauto = int(input("Inserisci il numero di automobili da registrare: "))

# Ciclo per raccogliere i dati delle automobili
for i in range(nauto):
    print(f"Inserisci i dati dell'automobile {i + 1}:")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = input("Anno di fabbricazione: ")

    # Creiamo un dizionario con i dati dell'automobile corrente
    automobile = {
        "Marca": marca,
        "Modello": modello,
        "Anno": anno
    }

    # Aggiungiamo il dizionario alla lista delle automobili
    lista_auto.append(automobile)

# Salviamo la lista di dizionari in un file JSON
with open("automobili.json", "w") as file_json:
    json.dump(lista_auto, file_json)

print("Dati delle automobili salvati correttamente nel file 'automobili.json'.")
