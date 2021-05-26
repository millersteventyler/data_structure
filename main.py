from linkedlist import LinkedList
from birthday import Birthday
from months import Months
from sweepstakes import Sweepstakes
from node2 import Node2

if __name__ == '__main__':

    pi_day = Months()
    print(f'Pi Day is in: {pi_day.calendar[2]}')
    birthday_location = Birthday()
    birthday_location.party_place.add('Texas')
    birthday_location.party_place.add('Florida')
    birthday_location.party_place.add('Alaska')
    print(f'{birthday_location.party_place}')

    winner = Sweepstakes()
    winner.random_winner()

    linked_list = LinkedList()
    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.add_to_beginning(50)

    if linked_list.contains_node(60):
        print("yes")
    else:
        print("no")

    r = Node2(50)
    r.insert_node(r, 30)
    r.insert_node(r, 30)
    r.insert_node(r, 20)
    r.insert_node(r, 40)
    r.insert_node(r, 70)
    r.insert_node(r, 60)
    r.insert_node(r, 80)

    r.inorder(r)

    r.search_for_node(r, 40)
    if r.search_for_node(r, 60):
        print("yes")
    else:
        print("no")
