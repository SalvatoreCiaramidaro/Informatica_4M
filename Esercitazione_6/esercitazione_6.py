import json

# Dizionario per la memorizzazione dei dati dei laboratori
laboratori = {}

# Caricamento dei dati da un file JSON se esiste
try:
    with open("laboratori.json", "r") as file:
        laboratori = json.load(file)
except FileNotFoundError:
    pass

# Funzione per aggiungere un laboratorio
def aggiungi_laboratorio(id_laboratorio, nome, n_pcs):
    laboratori[id_laboratorio] = {"nome": nome, "n_pcs": n_pcs}

# Funzione per stampare i laboratori disponibili
def stampa_laboratori_disponibili():
    for id_laboratorio, info in laboratori.items():
        print(f"ID: {id_laboratorio}, Nome: {info['nome']}, PC disponibili: {info['n_pcs']}")

# Funzione per cercare laboratori liberi in una certa fascia oraria
def cerca_laboratori_liberi(fascia_oraria):
    laboratori_liberi = []
    for id_laboratorio in laboratori:
        if id_laboratorio not in prenotazioni:
            laboratori_liberi.append(id_laboratorio)
    return laboratori_liberi

# Dizionario per la memorizzazione dei dati delle prenotazioni
prenotazioni = {}

# Funzione per aggiungere una prenotazione
def aggiungi_prenotazione(id_laboratorio, classe, docente, materia, giorno, orario):
    if id_laboratorio in prenotazioni:
        if giorno in prenotazioni[id_laboratorio]:
            prenotazioni[id_laboratorio][giorno][orario] = {"classe": classe, "docente": docente, "materia": materia}
        else:
            prenotazioni[id_laboratorio][giorno] = {orario: {"classe": classe, "docente": docente, "materia": materia}}
    else:
        prenotazioni[id_laboratorio] = {giorno: {orario: {"classe": classe, "docente": docente, "materia": materia}}}

# Funzione per rimuovere una prenotazione
def rimuovi_prenotazione(id_laboratorio, giorno, orario):
    if id_laboratorio in prenotazioni and giorno in prenotazioni[id_laboratorio] and orario in prenotazioni[id_laboratorio][giorno]:
        del prenotazioni[id_laboratorio][giorno][orario]
        if not prenotazioni[id_laboratorio][giorno]:
            del prenotazioni[id_laboratorio][giorno]

# Funzione per stampare il planning settimanale su un file di testo
def stampa_planning_settimanale():
    with open("planning_settimanale.txt", "w") as file:
        file.write("Orario\t\tLunedì\tMartedì\tMercoledì\tGiovedì\tVenerdì\n")
        for orario in orari:
            file.write(orario + "\t")
            for giorno in giorni_settimana:
                prenotazione = str(prenotazioni.get(giorno, {}).get(orario, ""))
                file.write(prenotazione + "\t")
            file.write("\n")

# Funzione per ripulire il planning settimanale
def ripulisci_planning_settimanale():
    prenotazioni.clear()

# Definizione degli orari e giorni della settimana
orari = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]
giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"]

# Loop principale
while True:
    print("\nMenu:")
    print("1. Aggiungi laboratorio")
    print("2. Stampa laboratori disponibili")
    print("3. Cerca laboratori liberi in una certa fascia oraria")
    print("4. Aggiungi una prenotazione")
    print("5. Rimuovi una prenotazione")
    print("6. Stampa il planning settimanale su un file di testo")
    print("7. Ripulisci il planning settimanale")
    print("8. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        id_laboratorio = input("ID/Nome del laboratorio: ")
        nome = input("Nome del laboratorio: ")
        n_pcs = int(input("Numero di PC disponibili: "))
        aggiungi_laboratorio(id_laboratorio, nome, n_pcs)
    elif scelta == "2":
        stampa_laboratori_disponibili()
    elif scelta == "3":
        fascia_oraria = input("Inserisci la fascia oraria (es. 1st-2nd): ")
        laboratori_liberi = cerca_laboratori_liberi(fascia_oraria)
        print("Laboratori liberi nella fascia oraria:", laboratori_liberi)
    elif scelta == "4":
        id_laboratorio = input("ID del laboratorio: ")
        classe = input("Classe: ")
        docente = input("Docente: ")
        materia = input("Materia: ")
        giorno = input("Giorno (es. Lunedì): ")
        orario = input("Orario (es. 1st): ")
        aggiungi_prenotazione(id_laboratorio, classe, docente, materia, giorno, orario)
    elif scelta == "5":
        id_laboratorio = input("ID del laboratorio: ")
        giorno = input("Giorno (es. Lunedì): ")
        orario = input("Orario (es. 1st): ")
        rimuovi_prenotazione(id_laboratorio, giorno, orario)
    elif scelta == "6":
        stampa_planning_settimanale()
        print("Planning settimanale salvato su 'planning_settimanale.txt'")
    elif scelta == "7":
        ripulisci_planning_settimanale()
        print("Planning settimanale ripulito.")
    elif scelta == "8":
        # Salvataggio dei dati su un file JSON prima di uscire
        with open("laboratori.json", "w") as file:
            json.dump(laboratori, file)
        break
    else:
        print("Scelta non valida. Riprova.")