class List(object):
    def __init__(self):
        self.count = 0
        self.current = None
        self.first = None
        self.last = None

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

    def __len__(self):
        return self.count

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
        current = self.first
        previous = self.first
        for _ in range(key-1):
            previous = self.current
            self.current = self.current.next
        previous.next = current.next


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
l.append("get a house")
del l[1]
l.append("get a house")
for x in l:
    print(x)

