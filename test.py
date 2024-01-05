"""
Module de test pour vérifier le fonctionnement des classes et fonctions dans le programme TryCount.
"""

import unittest
from datetime import date
from creator import Creator
from main import InterfaceHandler
from total import Total, Remb
from libs.exception import ExceptionNotValidParameter, ExceptionNotValidFile, ExceptionNotInstance
from libs.count import Count
from libs.person import Person

a = Count("Oskour", 2, str(date.today()), "Justin", ["Flo"])
b = Count("Bonjour", 25, str(date.today()), "Antoine", ["Tony"])
c = Person("Justin")
d = Person("Tony")
e = Creator()
f = Total(e.count_list, e.person_list)


class TestCase(unittest.TestCase):

    def test_interface_handler_start(self):
        with self.assertRaises(ExceptionNotValidParameter):
            InterfaceHandler().start("help", f)
        with self.assertRaises(ExceptionNotValidParameter):
            InterfaceHandler().start(2, f)
        with self.assertRaises(ExceptionNotValidParameter):
            InterfaceHandler().start(None, f)
        with self.assertRaises(ExceptionNotValidParameter):
            InterfaceHandler().start(e, "help")
        with self.assertRaises(ExceptionNotValidParameter):
            InterfaceHandler().start(e, 2)
        with self.assertRaises(ExceptionNotValidParameter):
            InterfaceHandler().start(e, None)


    def test_creator_write_file(self):
        with self.assertRaises(ExceptionNotValidFile):
            Creator().write_file([a, b], "oskour.png")
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

    def test_count_init(self):
        """
        title: str - Nom de la transaction
        amount: float - Montant de la transaction
        date: str - Date de la transaction
        has_paid: str - Nom de la personne qui a payé
        has_to_pay: list - Liste de toutes les personnes devant rembourser pour la transaction
        """
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", "txt", str(date.today()), "Justin", ["Flo"]) #Test avec du texte comme montant
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", None, str(date.today()), "Justin", ["Flo"]) #Test avec un montant nul
        self.assertRaises(ExceptionNotValidParameter, Count, "Titre", -1, str(date.today()), "Justin", ["Flo"]) #Test avec un montant négatif
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
        self.assertRaises(ExceptionNotValidParameter, Person, None)
        self.assertRaises(ExceptionNotValidParameter, Person, 1)
        self.assertRaises(ExceptionNotValidParameter, Person, [])

    def test_person_display(self):
        with self.assertRaises(ExceptionNotValidParameter):
            c.display_person(None)
        with self.assertRaises(ExceptionNotValidParameter):
            c.display_person("Oskour")
        with self.assertRaises(ExceptionNotValidParameter):
            c.display_person([])

    def test_total_init(self):
        self.assertRaises(ExceptionNotValidParameter, Total, 2, [c, d])
        self.assertRaises(ExceptionNotValidParameter, Total, [a, b], "")
        self.assertRaises(ExceptionNotValidParameter, Total, None, None)
        self.assertRaises(ExceptionNotInstance, Total, [a, b], ["Slt", None])
        self.assertRaises(ExceptionNotInstance, Total, [None, 2], [c, d])

    def test_remb(self):
        self.assertRaises(ExceptionNotValidParameter, Remb, "bjr", "Justin", "Flo")
        self.assertRaises(ExceptionNotValidParameter, Remb, 30, "Oskour", 25)
        self.assertRaises(ExceptionNotValidParameter, Remb, None, None, None)

if __name__ == '__main__':
    # ATTENTION : Pour exécuter ce test dans un notebook, il faut utiliser un appel à unittest.main() modifié.
    # Dans PyCharm, vous pouvez utiliser la version normale sans paramètre, cfr ci-dessous.
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
