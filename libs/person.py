"""
Module pour gérer les informations sur les personnes.

"""

from libs.exception import ExceptionNotValidParameter


class Person:
    """
    Cette classe définit un objet Person pour représenter une personne,
    comprenant des détails tels que le nom, l'IBAN et le compte PayPal.
    """

    def __init__(self, name, iban="", paypal=""):
        """ Construit un objet Count en fonction des valeurs données en paramètre

        PRE: name: str - Nom de la personne
        PRE: iban: Non obligatoire
        PRE: paypal: Non obligatoire
        """
        if not isinstance(name, str):
            raise ExceptionNotValidParameter
        self.name = name
        if iban == "":
            self.iban = "Non spécifié"
        else:
            self.iban = iban
        if paypal == "":
            self.paypal = "Non spécifié"
        else:
            self.paypal = paypal

    def display_person(self, order):
        """ Fonction qui affiche la personne

        PRÉ : order: int - ordre dans la liste des personnes
        POST : affichage de la personne
        """
        if not isinstance(order, int):
            raise ExceptionNotValidParameter
        print(f"{order} - Nom: {self.name}, IBAN: {self.iban}, Paypal: {self.paypal}")
