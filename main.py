"""
Module principal pour la gestion des dépenses, des participants, des remboursements, et des soldes.
"""
from creator import Creator
from total import Total
from libs.exception import ExceptionNotValidParameter


class InterfaceHandler:
    """Gère l'affichage de l'interface en ligne de commande.

            Cette classe fournit des méthodes pour interagir avec l'utilisateur via la ligne de commande.
            Elle inclut des fonctionnalités pour gérer les dépenses, les participants, les remboursements et les soldes.
            """
    def start(self, crea, tot):
        """Fonction qui gère l'affichage de l'interface."""
        if not isinstance(crea, Creator) or not isinstance(tot, Total):
            raise ExceptionNotValidParameter
        while True:
            print("\n" * 10)
            print(
                "0 - Dépenses \n1 - Participants \n2 - Voir les remboursements à faire \n3 - Voir les équilibres")
            inp = input(">>>>")
            while not inp.isdigit():
                print("Not a number")
                inp = input(">>>>")
            inp = int(inp)
            # depense
            if inp == 0:
                print("\n" * 10)
                print("0 - Ajouter une dépense\n1 - Supprimer une dépense\n2 - Voir les dépenses\n3 - Retour")
                inp2 = input(">>>>")
                while not inp2 in ["0", "1", "2", "3"]:
                    print("Not a valid number")
                    inp2 = input(">>>>")
                inp2 = int(inp2)
                if inp2 == 0:
                    print("\n" * 10)
                    crea.create_count()
                    j = 0
                    for i in crea.count_list:
                        i.display_count(j)
                        j += 1
                    input("Indiquez nimporte quelle valeur pour continuer >>")
                elif inp2 == 1:
                    print("\n" * 10)
                    j = 0
                    for i in crea.count_list:
                        i.display_count(j)
                        j += 1
                    print("'cancel' pour annuler l'oppération")
                    inp3 = input(">>>>")
                    while not inp3.isdigit() and not inp3 == "cancel":
                        print("Not a number")
                        inp3 = input(">>>>")
                    if not inp3 == "cancel":
                        inp3 = int(inp3)
                        crea.delete(inp3, "payment.json")
                elif inp2 == 2:
                    print("\n" * 10)
                    j = 0
                    for i in crea.count_list:
                        i.display_count(j)
                        j += 1
                    input("Indiquez nimporte quelle valeur pour continuer >>")
            # Choix Participants
            if inp == 1:
                print("\n" * 10)
                print("0 - Ajouter un Participant\n1 - Supprimer un Participant\n2 - Voir les Participants\n3 - Retour")
                inp2 = input(">>>>")
                while not inp2 in ["0", "1", "2", "3"]:
                    print("Not a valid number")
                    inp2 = input(">>>>")
                inp2 = int(inp2)
                if inp2 == 0:
                    print("\n" * 10)
                    crea.add_person()
                elif inp2 == 1:
                    print("\n" * 10)
                    j = 0
                    for i in crea.person_list:
                        i.display_person(j)
                        j += 1
                    print("'cancel' pour annuler l'oppération")
                    inp3 = input(">>>>")
                    while not inp3.isdigit() and not inp3 == "cancel":
                        print("Not a number")
                        inp3 = input(">>>>")
                    if not inp3 == "cancel":
                        inp3 = int(inp3)
                        crea.delete(inp3, "person.json")
                elif inp2 == 2:
                    print("\n" * 10)
                    j = 0
                    for i in crea.person_list:
                        i.display_person(j)
                        j += 1
                    input("Indiquez nimporte quelle valeur pour continuer >>")
            # Remboursements
            if inp == 2:
                print("\n" * 10)
                tot.display_remb()
                input("Indiquez nimporte quelle valeur pour continuer >>")
            # Equilibre
            if inp == 3:
                print("\n" * 10)
                tot.get_remb()
                for i in tot.sorted_list:
                    if i[1] > 0:
                        print(f"{i[0]}  +{round(i[1], 2)}€")
                    if i[1] == 0:
                        print(f"{i[0]}  0€")
                    if i[1] < 0:
                        print(f"{i[0]}  {round(i[1], 2)}€")
                input("Indiquez nimporte quelle valeur pour continuer >>")


if __name__ == "__main__":
    a = Creator()
    d = Total(a.count_list, a.person_list)
    InterfaceHandler().start(a, d)
