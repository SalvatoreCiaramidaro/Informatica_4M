import json

# Funzione per calcolare la rata del bollo per un modello di auto
def calcola_rata_bollo(marca, modello, anno):
    kW = 0  # Dovresti ottenere la potenza in kW basata su marca, modello o altri dati
    if kW <= 100:
        return 2.58 * kW
    else:
        return 2.58 * 100 + 3.87 * (kW - 100)

# Funzione per calcolare l'età media degli autoveicoli nella lista
def calcola_eta_media(lista_auto):
    oggi = 2023  # Puoi sostituire con l'anno corrente
    somma_eta = 0
    num_auto = len(lista_auto)
    for auto in lista_auto:
        anno_immatricolazione = int(auto['Anno'])
        eta_auto = oggi - anno_immatricolazione
        somma_eta += eta_auto
    return somma_eta / num_auto

# Leggi il file JSON con f.read()
with open('registrazioneautomobili.json', 'r') as file:
    json_data = file.read()
    
lista_auto = json.loads(json_data)

for auto in lista_auto:
    marca_auto = auto['Marca']
    modello_auto = auto['Modello']
    anno_immatricolazione = auto['Anno']
    rata_bollo = calcola_rata_bollo(marca_auto, modello_auto, anno_immatricolazione)
    print(f"La rata del bollo per l'auto {marca_auto} {modello_auto} è: {rata_bollo:.2f} euro")

eta_media = calcola_eta_media(lista_auto)
print(f"L'età media delle auto nella lista è: {eta_media:.2f} anni")
