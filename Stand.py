class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.espositore = None
        self.disponibile = True

    def calcola_prezzo(self):
        return self.prezzo_base

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice == other.codice
        return False

    #usato per insegnare al programma come ordinare o confrontare due oggetti
    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.calcola_prezzo() < other.calcola_prezzo()
        return NotImplemented


class StandStandard(Stand):
    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Occupato da {self.espositore.codice}"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.numero_prese = int(numero_prese)
        self.espositore = None
        self.disponibile = True

    def calcola_prezzo(self):

        return self.prezzo_base * (1 + 0.07 * self.numero_prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Occupato da {self.espositore.codice}"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self.numero_prese} - {stato}"


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.posizione = posizione
        self.espositore = None
        self.disponibile = True

    def calcola_prezzo(self):

        return self.prezzo_base * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Occupato da {self.espositore.codice}"
        return f"{self.codice}: Premium ({self.posizione}) | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"