"""
Module de test pour vérifier le fonctionnement des classes et fonctions dans le programme TryCount.
"""

import unittest
from datetime import date
from creator import Creator
from total import Total, Remb
from libs.exception import ExceptionNotValidParameter, ExceptionNotValidFile
from libs.count import Count
from libs.person import Person

a = Count("Titre", 2, str(date.today()), "Justin", ["Flo"])
b = Count("Bonjour", 25, str(date.today()), "Antoine", ["Tony"])
c = Person("Justin")
d = Person("Tony")
e = Creator()
f = Total(e.count_list, e.person_list)


class TestCase(unittest.TestCase):

    def test_count_init(self):
        """
        title: str - Nom de la transaction
        amount: float - Montant de la transaction
        date: str - Date de la transaction
        has_paid: str - Nom de la personne qui a payé
        has_to_pay: list - Liste de toutes les personnes devant rembourser pour la transaction
        """
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", "txt", str(date.today()), "Justin", ["Flo"]) #Test avec du texte comme montant
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", None, str(date.today()), "Justin", ["Flo"]) #Test avec un montant Nul
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", 10, str(date.today()), "Justin", "NotAList") #Test si la liste est bien une liste
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", 10, str(date.today()), None, ["Flo"]) #Test avec une personne est Nul
        self.assertRaises(ExceptionNotValidParameter, Count, None, 10, str(date.today()), "Justin", ["Flo"]) #Test avec nom de transaction Nul

    def test_count_display(self):
        with self.assertRaises(ExceptionNotValidParameter):
            a.display_count(None)
        with self.assertRaises(ExceptionNotValidParameter):
            a.display_count("Oskour")
        with self.assertRaises(ExceptionNotValidParameter):
            a.display_count([])

    def test_person_init(self):
        """
        name: str - Nom de la personne
        """
        self.assertRaises(ExceptionNotValidParameter, Person, None) #Test si la personne est 'None'
        self.assertRaises(ExceptionNotValidParameter, Person, 1) #Test si le nom de la personne est un nombre
        self.assertRaises(ExceptionNotValidParameter, Person, []) #Test si le nom de la personne est une liste vide

    def test_person_display(self):
        with self.assertRaises(ExceptionNotValidParameter):
            c.display_person(None)
        with self.assertRaises(ExceptionNotValidParameter):
            c.display_person("Oskour")
        with self.assertRaises(ExceptionNotValidParameter):
            c.display_person([])

    def test_total_init(self):
        self.assertRaises(ExceptionNotValidParameter, Total, 2, [c, d]) #Test si la liste Count est un entier
        self.assertRaises(ExceptionNotValidParameter, Total, [a, b], "") #Test si la liste Person est une chaine vide
        self.assertRaises(ExceptionNotValidParameter, Total, None, None) #Test si les 2 arguments sont des None


    def test_remb(self):
        self.assertRaises(ExceptionNotValidParameter, Remb, "bjr", "Justin", "Flo")
        self.assertRaises(ExceptionNotValidParameter, Remb, 30, "Oskour", 25)
        self.assertRaises(ExceptionNotValidParameter, Remb, None, None, None)

    def test_creator_write_file(self):
        with self.assertRaises(ExceptionNotValidFile):
            Creator().write_file([a, b], "test.png")
        with self.assertRaises(ExceptionNotValidFile):
            Creator().write_file([a, b], "bonjour.json.png")
        with self.assertRaises(ExceptionNotValidFile):
            Creator().write_file([a, b], [])
        with self.assertRaises(ExceptionNotValidFile):
            Creator().write_file([a, b], 2)
        with self.assertRaises(ExceptionNotValidFile):
            Creator().write_file([a, b], None)
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().write_file("", "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().write_file(None, "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().write_file(2, "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().write_file(["", ""], "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().write_file([None, None], "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().write_file([2, 2], "a.json")

    def test_creator_delete(self):
        with self.assertRaises(ExceptionNotValidFile):
            Creator().delete(2, "oskour.png")
        with self.assertRaises(ExceptionNotValidFile):
            Creator().delete(2, "bonjour.json.png")
        with self.assertRaises(ExceptionNotValidFile):
            Creator().delete(2, [])
        with self.assertRaises(ExceptionNotValidFile):
            Creator().delete(2, 2)
        with self.assertRaises(ExceptionNotValidFile):
            Creator().delete(2, None)
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().delete("", "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().delete(None, "a.json")
        with self.assertRaises(ExceptionNotValidParameter):
            Creator().delete([], "a.json")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
