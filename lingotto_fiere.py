import csv
from Espositore import Espositore
from Stand import StandStandard, StandPreseExtra, StandPremium

class LingottoFiere:
    def __init__(self, nome):
        self._nome = nome
        self.stand = {}
        self.espositori = {}

    # permette di leggere il nome di un attributo protetto
    @property
    def nome(self):
        return self._nome

    #Permette di modificare o assegnare un nuovo valore all'attributo in modo controllato.
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        try:
            with open(file_path, mode= "r", encoding='utf-8') as file:
                for riga in file:
                    if not riga:
                        continue
                    parti = riga.strip().split(",")
                    codice = parti[0]

                    if codice.startswith("ST"):
                        superficie = parti[1]
                        padiglione = parti[2]
                        prezzo_base = parti[3]

                        nuovo_stand = None
                        if len(parti) == 4:
                            nuovo_stand = StandStandard(codice, superficie, padiglione, prezzo_base)
                        elif len(parti) >= 5:
                            valore_aggiuntivo = parti[4]
                            if valore_aggiuntivo.isdigit():
                                nuovo_stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, valore_aggiuntivo)
                            else:
                                nuovo_stand = StandPremium(codice, superficie, padiglione, prezzo_base, valore_aggiuntivo)

                        self.stand[codice] = nuovo_stand

                    elif codice.startswith("ES"):
                        if len(parti) < 3:
                            continue
                        nome = parti[1]
                        cognome = parti[2]
                        nuovo_espositore = Espositore(codice, nome, cognome)
                        self.espositori[codice] = nuovo_espositore
        except FileNotFoundError:
            raise FileNotFoundError(f"Il file specificato '{file_path}' non è stato trovato.")



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):

        if codice_stand not in self.stand:
            raise ValueError(f"Lo stand con codice '{codice_stand}' non esiste.")

        if codice_espositore not in self.espositori:
            raise ValueError(f"L'espositore con codice '{codice_espositore}' non esiste.")

        s = self.stand[codice_stand]
        e = self.espositori[codice_espositore]

        if not s.disponibile:
            raise ValueError(f"Lo stand '{codice_stand}' è già occupato.")

        if e.stand_assegnato is not None:
            raise ValueError(f"L'espositore '{codice_espositore}' ha già uno stand assegnato.")

        # Se tutti i controlli passano, eseguiamo l'assegnazione
        s.disponibile = False
        s.espositore = e
        e.stand_assegnato = s



    def elenca_espositori(self):
        """Stampa l'elenco di tutti gli espositori registrati e il relativo stand se assegnato."""
        if not self.espositori:
            print("Nessun espositore registrato nel sistema.")
            return

        print("\n--- ELENCO ESPOSITORI ---")
        for espositore in self.espositori.values():
            print(espositore)

    def stand_ordinati_per_prezzo(self):
            """Restituisce la lista degli stand ordinati dal più economico al più costoso."""
            # sorted() utilizza automaticamente il metodo __lt__ definito nella classe Stand
            return sorted(self.stand.values())
