class Espositore:

    def __init__(self,codice,nome,cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand_assegnato = None

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.codice == other.codice
        return False

    def __str__(self):
        stand_info = f" - Stand: {self.stand_assegnato.codice}" if self.stand_assegnato else " - Nessuno stand assegnato"
        return f"Espositore {self.codice}: {self.nome} {self.cognome}{stand_info}"
    