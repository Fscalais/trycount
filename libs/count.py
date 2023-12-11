from libs.exception import *


class Count:

    def __init__(self, title, amount, date, has_paid, has_to_pay):
        """ Builds a Count based of the values given in parameter

        PRE: title: str - Name of the transaction
        PRE: amount: float - Price of the count
        PRE: date: str - Date of the transaction
        PRE: has_paid: str - Name of the person that paid
        PRE: has_to_pay: list - List of all peoples that need to reimburse for the count
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
