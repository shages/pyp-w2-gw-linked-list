class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    #: Value of the node
    _elem = None

    #: Pointer to the next item in the list
    _next = None

    def __init__(self, elem, next=None):
        self._elem = elem
        if next:
            self._next = next

    def __str__(self):
        str = 'Node({0}) >'.format(self.elem)
        if self.next is not None:
            str = '{0} Node({1})'.format(str, self.next.elem)
        else:
            str = '{0} /'.format(str)
        return str

    def __eq__(self, other):
        return self.elem == other.elem

    def __repr__(self):
        return str(self.elem)

    @property
    def elem(self):
        return self._elem

    @elem.setter
    def elem(self, elem):
        self._elem = elem

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

