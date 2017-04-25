from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    #: Pointer to the first node in the list
    _start = None

    #: Pointer to the last node in the list
    _end = None

    #: The current l ength of the list
    _length = 0

    def __init__(self, elements=None):
        if not elements:
            return

        for item in elements:
            self.append(item)

    def __str__(self):
        return '[{0}]'.format(', '.join([str(v) for v in [c.elem for c in list(self)]]))

    def __len__(self):
        return self.count()

    def __iter__(self):
        return LinkedListIterator(self._start)

    def __getitem__(self, index):
        return list(self)[index].elem

    def __add__(self, other):
        new_obj = LinkedList()
        item = self._start
        while item is not None:
            new_obj.append(item.elem)
            item = item.next

        new_obj += other
        return new_obj

    def __iadd__(self, other):
        for item in other:
            self.append(item.elem)
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for (him, her) in zip(list(self), list(other)):
            if him != her:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def append(self, elem):
        new_node = Node(elem)
        self._length += 1
        if self._end:
            self._end.next = new_node
            self._end = new_node
        else:
            self._start = new_node
            self._end = new_node
            self._curr = new_node

    def count(self):
        return self._length

    def pop(self, index=None):
        if index is None:
            last = self._end

            if last is None:
                raise IndexError

            # Update _end if necessary
            if self._start != self._end:
                item = self._start
                while item.next != self._end:
                    item = item.next
                item.next = None
                self._end = item
            else:
                self._start = None
                self._end = None

            self._length -= 1
            return last.elem

        # we have an index
        c = 0
        prev = None
        for item in self:
            if c == index:
                # pop this guy
                if prev:
                    prev.next = item.next
                else:
                    # start
                    self._start = item.next
                break
            prev = item
            c += 1

        if c == len(self):
            # not found
            raise IndexError

        if item is None:
            # null value - empty list
            raise IndexError

        self._length -= 1
        return item.elem

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def length(self):
        return self._length

class LinkedListIterator(object):
    _start = None
    def __init__(self, start):
        self._start = start

    def __next__(self):
        if self._start is None:
            raise StopIteration
        item = self._start
        self._start = self._start.next
        return item

