from libs.count import Count
from libs.person import Person
from libs.exception import *
from creator import isfloat


class Remb:
    """ Class representing a reimbursement proposition
    """

    def __init__(self, amount, has_remb, has_been_remb):
        if not isfloat(amount) or not isinstance(has_remb, str) or not isinstance(has_been_remb, str):
            raise ExceptionNotValidParameter
        self.amount = amount
        self.has_remb = has_remb
        self.has_been_remb = has_been_remb


class Total:

    def __init__(self, count_list, person_list):
        """ """
        if isinstance(count_list, list) and isinstance(person_list, list):
            for i in count_list:
                if not isinstance(i, Count):
                    raise ExceptionNotInstance
            for i in person_list:
                if not isinstance(i, Person):
                    raise ExceptionNotInstance
        else:
            raise ExceptionNotValidParameter
        self.remb_list = []
        self.sorted_list = []
        self.count_list = count_list
        self.person_list = person_list

    def get_remb(self):
        """ Function calculating every Reimbursement and adds them to the list (remb_list)

        POST: list - remb_liste the list containing instances of Remb
        """
        positive = []
        negative = []
        ratio = {}
        self.remb_list = []
        for i in self.person_list:
            ratio[i.name] = 0

        for i in self.count_list:
            for j in i.has_to_pay: ratio[j] -= i.amount / len(i.has_to_pay)
            ratio[i.has_paid] += i.amount

        self.sorted_list = sorted(ratio.items(), key=lambda t: t[1])
        for i in self.sorted_list:
            if i[1] > 0:
                positive.append(list(i))
            elif i[1] < 0:
                negative.append(list(i))
        positive.reverse()
        for i in negative:
            for j in positive:
                if abs(i[1]) > j[1] and not j[1] == 0:
                    self.remb_list.append(Remb(round(j[1], 2), i[0], j[0]))
                    i[1] += j[1]
                    j[1] = 0
                if abs(i[1]) == j[1] and not j[1] == 0 and not i[1] == 0:
                    self.remb_list.append(Remb(round(j[1], 2), i[0], j[0]))
                    i[1] = 0
                    j[1] = 0
                if abs(i[1]) < j[1] and not j[1] == 0 and not i[1] == 0:
                    self.remb_list.append(Remb(round(abs(i[1]), 2), i[0], j[0]))
                    j[1] += i[1]
                    i[1] = 0
        return self.remb_list

    def display_remb(self):
        """ Function that's printing the reimbursements

        POST: prints of every reimbursements
        """
        count = 0
        for i in self.get_remb():
            print(f"{count} - {i.has_remb} doit rembouser {i.amount}€ à {i.has_been_remb}")
            count += 1
