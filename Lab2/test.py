class LinkedList:
    head: 'Node'
    tail: 'Node'

    def __init__(self, wartosc, nastepny):
        self.value = wartosc
        self.next = nastepny