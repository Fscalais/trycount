"""
Module de création et de gestion des données pour Tricount.
Ce module définit la classe Creator pour gérer la création, la modification et la suppression des données.
"""

import json
from datetime import date
from libs.count import Count
from libs.person import Person
from libs.exception import ExceptionNotValidParameter, ExceptionNotValidFile


class Creator:
    """
    Classe pour la création, la modification et la suppression des données pour Tricount.

    Cette classe permet d'accéder aux fichiers JSON, d'ajouter des valeurs aux listes,
    de créer un nouveau compte, de supprimer une instance, et d'ajouter une personne.
    """
    def __init__(self):
        """ Access the json files and add the values to lists
        """
        self.count_list = []
        with open("payments.json", encoding="utf-8") as file:
            data = json.load(file)
        for i in data:
            self.count_list.append(Count(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
        self.person_list = []
        with open("person.json", encoding="utf-8") as file:
            data_person = json.load(file)
        for i in data_person:
            self.person_list.append(Person(data_person[i][0], data_person[i][1], data_person[i][2]))

    def write_file(self, lst, file):
        """ Function that overwrites the json file with the new values

        PRE: lst: list - to be added to a json file
        PRE: file: sting - json file to be written tot
        """
        if not isinstance(file, str) or not file.rsplit(".", 1)[1] == "json":
            raise ExceptionNotValidFile
        if not isinstance(lst, list):
            raise ExceptionNotValidParameter
        else:
            for i in lst:
                if not isinstance(i, Count) and not isinstance(i, Person):
                    raise ExceptionNotValidParameter
        j = 0
        obj = {}
        for i in lst:
            obj[j] = [i.title, i.amount, i.date, i.has_paid, i.has_to_pay]
            j += 1
        with open(file, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(obj))

    def create_count(self):
        """ Function that create a count, ask for thoses values at the user with inputs.
        Afterwards call write_file to update the file
        """
        print("Titre")
        title = input(">>>>")
        print("Montant")
        amount = input(">>>>")
        while not isfloat(amount):
            print("Merci d'indiquer un montant correct")
            amount = input(">>>>")
        print("A payé")
        has_paid = input(">>>>")
        names = []
        for i in self.person_list:
            names.append(i.name)
        while not has_paid in names:
            print("Le nom indiqué n'est pas dans les Paticipants du Tricount, veuilliez indiquer un nom correct")
            has_paid = input(">>>>")
        print("Doit rembourser, écrivez 'stop' pour arreter")

        hp = input(">>>>")
        while not has_paid in names:
            print("Le nom indiqué n'est pas dans les Paticipants du Tricount, veuilliez indiquer un nom correct")
            hp = input(">>>>")
        tot = []
        while not hp == "stop":
            if hp in names:
                tot.append(hp)
            else:
                print("Le nom indiqué n'est pas dans les Paticipants du Tricount, veuilliez indiquer un nom correct")
            hp = input(">>>>")
        self.count_list.append(Count(title, amount, str(date.today()), has_paid, tot))
        self.write_file(self.count_list, "payments.json")

    def delete(self, choice, file):
        """ Function that deletes an instance of count or person in the list

        PRE: choice: int - choice of the instance the user want to delete
        PRE: file: str - name of the json file where thoses values are stored
        """
        if not isinstance(choice, int):
            raise ExceptionNotValidParameter
        if not isinstance(file, str) or not file.rsplit(".", 1)[1] == "json":
            raise ExceptionNotValidFile
        del self.count_list[choice]
        self.write_file(self.count_list, file)

    def add_person(self):
        """ Function that asks for the user to input the values to add a person
        """
        print("Nom")
        name = input(">>>>")
        print("IBAN")
        iban = input(">>>>")
        print("Paypal")
        paypal = input(">>>>")
        self.person_list.append(Person(name, iban, paypal))
        self.write_file(self.person_list, "person.json")


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
