"""
Module principal pour la gestion des dépenses, des participants, des remboursements, et des soldes.
"""
from creator import Creator
from total import Total
from libs.exception import ExceptionNotValidParameter


class InterfaceHandler:
    """
    Gère l'affichage de l'interface en ligne de commande.

    Cette classe fournit des méthodes pour interagir avec l'utilisateur via la ligne de commande.
    Elle inclut des fonctionnalités pour gérer les dépenses, les participants, les remboursements et les soldes.
    """

    def __init__(self, crea, tot):
        if not isinstance(crea, Creator) or not isinstance(tot, Total):
            raise ExceptionNotValidParameter
        self.crea = crea
        self.tot = tot

    def display_expenses_menu(self):
        """
        Affiche le menu des dépenses dans l'interface en ligne de commande.

        Le menu permet d'effectuer les opérations suivantes :
        0 - Ajouter une dépense
        1 - Supprimer une dépense
        2 - Voir les dépenses
        3 - Retour
        """
        print("\n" * 10)
        print("0 - Ajouter une dépense\n1 - Supprimer une dépense\n2 - Voir les dépenses\n3 - Retour")
        inp2 = input(">>>>")
        while not inp2 in ["0", "1", "2", "3"]:
            print("Not a valid number")
            inp2 = input(">>>>")
        inp2 = int(inp2)
        if inp2 == 0:
            print("\n" * 10)
            self.crea.create_count()
            j = 0
            for i in self.crea.count_list:
                i.display_count(j)
                j += 1
            input("Indiquez n'importe quelle valeur pour continuer >>")
        elif inp2 == 1:
            print("\n" * 10)
            j = 0
            for i in self.crea.count_list:
                i.display_count(j)
                j += 1
            print("'cancel' pour annuler l'opération")
            inp3 = input(">>>>")
            while not inp3.isdigit() and not inp3 == "cancel":
                print("Not a number")
                inp3 = input(">>>>")
            if not inp3 == "cancel":
                inp3 = int(inp3)
                self.crea.delete(inp3, "payment.json")
        elif inp2 == 2:
            print("\n" * 10)
            j = 0
            for i in self.crea.count_list:
                i.display_count(j)
                j += 1
            input("Indiquez n'importe quelle valeur pour continuer >>")

    def display_participants_menu(self):
        """
         Affiche le menu des participants dans l'interface en ligne de commande.

        Le menu permet d'effectuer les opérations suivantes :
        0 - Ajouter un Participant
        1 - Supprimer un Participant
        2 - Voir les Participants
        3 - Retour
        """
        print("\n" * 10)
        print("0 - Ajouter un Participant\n1 - Supprimer un Participant\n2 - Voir les Participants\n3 - Retour")
        inp2 = input(">>>>")
        while not inp2 in ["0", "1", "2", "3"]:
            print("Not a valid number")
            inp2 = input(">>>>")
        inp2 = int(inp2)
        if inp2 == 0:
            print("\n" * 10)
            self.crea.add_person()
        elif inp2 == 1:
            print("\n" * 10)
            j = 0
            for i in self.crea.person_list:
                i.display_person(j)
                j += 1
            print("'cancel' pour annuler l'opération")
            inp3 = input(">>>>")
            while not inp3.isdigit() and not inp3 == "cancel":
                print("Not a number")
                inp3 = input(">>>>")
            if not inp3 == "cancel":
                inp3 = int(inp3)
                self.crea.delete(inp3, "person.json")
        elif inp2 == 2:
            print("\n" * 10)
            j = 0
            for i in self.crea.person_list:
                i.display_person(j)
                j += 1
            input("Indiquez n'importe quelle valeur pour continuer >>")

    def display_interface(self):
        """
        Affiche l'interface en ligne de commande permettant d'interagir avec les dépenses, les participants,
        les remboursements et les soldes.

        Utilise les objets Creator et Total passés en paramètres pour effectuer les opérations.
        """
        while True:
            print("\n" * 10)
            print("0 - Dépenses \n1 - Participants \n2 - Voir les remboursements à faire \n3 - Voir les équilibres")
            inp = input(">>>>")
            while not inp.isdigit():
                print("Not a number")
                inp = input(">>>>")
            inp = int(inp)

            if inp == 0:
                self.display_expenses_menu()
            elif inp == 1:
                self.display_participants_menu()
            elif inp == 2:
                print("\n" * 10)
                self.tot.display_remb()
                input("Indiquez n'importe quelle valeur pour continuer >>")
            elif inp == 3:
                print("\n" * 10)
                self.tot.get_remb()
                for i in self.tot.sorted_list:
                    if i[1] > 0:
                        print(f"{i[0]}  +{round(i[1], 2)}€")
                    if i[1] == 0:
                        print(f"{i[0]}  0€")
                    if i[1] < 0:
                        print(f"{i[0]}  {round(i[1], 2)}€")
                input("Indiquez n'importe quelle valeur pour continuer >>")


if __name__ == "__main__":
    a = Creator()
    d = Total(a.count_list, a.person_list)
    InterfaceHandler(a, d).display_interface()
