class List(object):
    def __init__(self):
        self.count = 0
        self.first = None
        self.last = None
        self.iter_object = None

    def __iter__(self):
        self.iter_object = self.iterate()
        return self

    def __next__(self):
        element = next(self.iter_object)
        return element.value

    def __len__(self):
        return self.count

    def __str__(self):
        return str([x for x in self])

    def iterate(self):
        current = self.first
        while current is not None:
            yield current
            current = current.next
        raise StopIteration

    def init_empty(self, value):
        if self.last is None and self.first is None:
            element = Element(value=value)
            self.last = element
            self.first = element
            return True
        return False

    def __delitem__(self, key):
        if key >= self.count:
            raise ValueError
        self.count -= 1
        if key == 0:
            self.first = self.first.next
            return

        current = self.first
        previous = self.first
        for _ in range(key):
            previous = current
            current = current.next
        previous.next = current.next

    def remove(self, value):
        self.count -= 1
        if value == self.first.value:
            self.first = self.first.next
            return

        current = self.first
        previous = self.first
        for _ in range(len(self)-1):
            previous = current
            current = current.next
            if value == current.value:
                previous.next = current.next
                return
        self.count += 1
        raise ValueError

    def append(self, value):
        self.count += 1
        if not self.init_empty(value):
            element = Element(value=value, next=None)
            self.last.next = element
            self.last = element

    def append_left(self, value):
        self.count += 1
        if not self.init_empty(value):
            element = Element(value=value, next=self.first)
            self.first = element


class Element(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


l = List()
l.append("loool")
l.append("get a house")
l.append("get a house2")
print(l)
l.remove("get a house")
print(l)

