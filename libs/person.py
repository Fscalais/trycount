from libs.exception import *


class Person:

    def __init__(self, name, iban="", paypal=""):
        """ Builds a Count based of the values given in parameter

        PRE: name: str - Name of the person
        PRE: iban: Not obligatory, if not specified indicates it
        PRE: paypal: Not obligatory, if not specified indicates it
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
        """ Function that prints the person

        PRE: order: int - order in the list of person
        POST: print of the count
        """
        if not isinstance(order, int):
            raise ExceptionNotValidParameter
        print(f"{order} - Nom: {self.name}, IBAN: {self.iban}, Paypal: {self.paypal}")
