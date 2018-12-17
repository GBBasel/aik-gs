from random import shuffle
import time


def bubblesort(l):
    for rounds in range(len(l) - 1, 0, -1):
        for i in range(rounds):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]


def bubblesort1(l):
    switched = len(l) - 1
    while switched:
        last = switched
        switched = 0
        for i in range(last):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                switched = i + 1


def quicksort(l):
    if not l:
        return []
    pivot = l[0]
    smaller = []
    greater = []
    for i in l[1:]:
        if i < pivot:
            smaller.append(i)
        else:
            greater.append(i)
    return quicksort(smaller) + [pivot] + quicksort(greater)


def test_cases(func, x=10000, n=20):
    s_t = time.time()
    for _ in range(x):
        l = list(range(n))
        func(l)
    print("best:", (time.time() - s_t))
    s_t = time.time()
    for _ in range(x):
        l = list(range(n))
        shuffle(l)
        func(l)
    print("average:", (time.time() - s_t))
    s_t = time.time()
    for _ in range(x):
        l = list(reversed(range(n)))
        func(l)
    print("worst:", (time.time() - s_t))


# test_cases(bubblesort)
# weil es immer durch die ganze liste geht und nicht den inhalt der liste berücksichtigt.

# test_cases(bubblesort1)
# best: 0.04687142372131348
# average: 1.0156784057617188
# worst: 1.1094439029693604

test_cases(quicksort)
# best: 0.5781078338623047
# average: 0.5781807899475098
# worst: 0.5156083106994629
