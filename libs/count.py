"""
Module pour la gestion des transactions financières.
Ce module définit la classe Count pour représenter une transaction financière.
"""

from libs.exception import ExceptionNotValidParameter


class Count:

    """
    Cette classe définit un objet Count pour représenter une transaction financière,
    comprenant des détails tels que le titre, le montant, la date, la personne ayant payé,
    et la liste des personnes devant rembourser.
    """

    def __init__(self, title, amount, date, has_paid, has_to_pay):
        """
        Construit un objet Count en utilisant les valeurs données en paramètre.

        PRÉ : title: str - Nom de la transaction
        PRÉ : amount: float - Montant de la transaction
        PRÉ : date: str - Date de la transaction
        PRÉ : has_paid: str - Nom de la personne qui a payé
        PRÉ : has_to_pay: list - Liste de toutes les personnes devant rembourser pour la transaction
        """
        if not isfloat(amount) or not isinstance(title, str) or not isinstance(has_paid,
                                                                               str) or not isinstance(
            date, str) or not isinstance(has_paid, str) or not isinstance(has_to_pay, list):
            raise ExceptionNotValidParameter
        self.title = title
        self.amount = float(amount)
        self.date = date
        self.has_paid = has_paid
        self.has_to_pay = has_to_pay

    def display_count(self, order):
        """ Function that prints the count

        PRE: order: int - order in the list of counts
        POST: print of the count
        """
        if not isinstance(order, int):
            raise ExceptionNotValidParameter
        pour = ", ".join(str(i) for i in self.has_to_pay)
        print(
            f"{order} - {self.title}, Prix: {self.amount}€, Date: {self.date}, A payé: {self.has_paid}, Pour: {pour}")


def isfloat(num):
    """ Function verifies if an input is float

    :return True if the input is float, False if the input is not
    """
    if num is None:
        return False
    try:
        float(num)
        return True
    except ValueError:
        return False
