import json

museo = {
    "stanze": {},
    "opere": {}
}

def crea_stanza(numero_stanza):
    if numero_stanza not in museo["stanze"]:
        museo["stanze"][numero_stanza] = []
        return True
    else:
        print("La stanza esiste già.")
        return False

def aggiungi_opera(numero_stanza, titolo, artista, anno):
    if numero_stanza in museo["stanze"]:
        opera = {"titolo": titolo, "artista": artista, "anno": anno}
        museo["stanze"][numero_stanza].append(opera)
        museo["opere"][titolo] = opera
        return True
    else:
        print("La stanza non esiste.")
        return False

def consulta_opere_in_stanza(numero_stanza):
    if numero_stanza in museo["stanze"]:
        opere = museo["stanze"][numero_stanza]
        if opere:
            for opera in opere:
                print(f"Titolo: {opera['titolo']}, Artista: {opera['artista']}, Anno: {opera['anno']}")
        else:
            print("La stanza è vuota.")
    else:
        print("La stanza non esiste.")

def consulta_stanze():
    stanze = museo["stanze"]
    if stanze:
        for numero_stanza in stanze:
            print(f"Stanza {numero_stanza}")
    else:
        print("Il museo non ha stanze.")

def cerca_informazioni_opera(titolo):
    if titolo in museo["opere"]:
        opera = museo["opere"][titolo]
        print(f"Titolo: {opera['titolo']}, Artista: {opera['artista']}, Anno: {opera['anno']}")
    else:
        print("Opera non trovata.")

def cancella_opera(titolo):
    if titolo in museo["opere"]:
        opera = museo["opere"].pop(titolo)
        for numero_stanza, opere in museo["stanze"].items():
            for o in opere:
                if o == opera:
                    opere.remove(o)
        return True
    else:
        print("Opera non trovata.")
        return False

def cancella_stanza(numero_stanza):
    if numero_stanza in museo["stanze"]:
        if not museo["stanze"][numero_stanza]:
            del museo["stanze"][numero_stanza]
            return True
        else:
            print("La stanza non è vuota.")
            return False
    else:
        print("La stanza non esiste.")
        return False

def salva_su_file():
    # Costruisci il percorso completo per il file JSON nella stessa cartella del file Python
    
    with open("museo.json", 'w') as file:
        json.dump(museo, file)
        print(f'Il file JSON è stato salvato correttamente')

def carica_da_file():
    # Costruisci il percorso completo per il file JSON nella stessa cartella del file Python
    
    try:
        with open("museo.json", 'r') as file:
            data = json.load(file)
            museo.update(data)
            print(f'Il file JSON è stato caricato correttamente')
    except FileNotFoundError:
        print("Il file JSON non è stato trovato nella stessa cartella del file Python.")

def menu():
    while True:
        print("\nMenu principale:")
        print("1. Creare una nuova stanza")
        print("2. Aggiungere un'opera ad una stanza")
        print("3. Consultare le opere presenti in una stanza")
        print("4. Consultare le stanze presenti")
        print("5. Cercare le informazioni su un'opera")
        print("6. Cancellare un'opera")
        print("7. Cancellare una stanza solo se vuota")
        print("8. Salva su file")
        print("9. Carica da file")
        print("0. Uscire")
        
        scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")

        if scelta == "1":
            numero_stanza = input("Inserisci il numero della stanza: ")
            crea_stanza(numero_stanza)
        elif scelta == "2":
            numero_stanza = input("Inserisci il numero della stanza: ")
            titolo = input("Inserisci il titolo dell'opera: ")
            artista = input("Inserisci l'artista dell'opera: ")
            anno = input("Inserisci l'anno dell'opera: ")
            aggiungi_opera(numero_stanza, titolo, artista, anno)
        elif scelta == "3":
            numero_stanza = input("Inserisci il numero della stanza: ")
            consulta_opere_in_stanza(numero_stanza)
        elif scelta == "4":
            consulta_stanze()
        elif scelta == "5":
            titolo = input("Inserisci il titolo dell'opera: ")
            cerca_informazioni_opera(titolo)
        elif scelta == "6":
            titolo = input("Inserisci il titolo dell'opera da cancellare: ")
            cancella_opera(titolo)
        elif scelta == "7":
            numero_stanza = input("Inserisci il numero della stanza da cancellare: ")
            cancella_stanza(numero_stanza)
        elif scelta == "8":
            salva_su_file()
        elif scelta == "9":
            carica_da_file()
        elif scelta == "0":
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu()