import random


class Sweepstakes:
    def __init__(self):
        self.contestant_ticket = {
            'person1': {
                'first_name': 'Steven',
                'last_name': 'Miller',
                'ticket_number': 1
            },
            'person2': {
                'first_name': 'Chelsee',
                'last_name': 'Miller',
                'ticket_number': 2
            },
            'person3': {
                'first_name': 'Jake',
                'last_name': 'Dugan',
                'ticket_number': 3
            },
            'person4': {
                'first_name': 'Charlie',
                'last_name': 'Steslick',
                'ticket_number': 4
            },
            'person5': {
                'first_name': 'Dylan',
                'last_name': 'Larkin',
                'ticket_number': 5
            }
        }

    def random_winner(self):
        winner = random.choice(list(self.contestant_ticket.values()))
        print(f'The sweepstakes winner is {winner["first_name"]}' + ' ' f'{winner["last_name"]}!')
