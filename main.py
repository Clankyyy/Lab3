import timeit

def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        mark = a[0]
        greater = []
        less = []
        for x in a[1:]:
            if x > mark:
                greater.append(x)
            else:
                less.append(x)
        b = []
        b.extend(quicksort(less))
        b.extend([mark])
        b.extend(quicksort(greater))
        return b

def rastsort(a):
    rng = int(len(a))
    flag = True
    while rng != 1 or flag:
        rng = max(1, int(rng - 1))
        flag = False
        for i in range(len(a) - rng):
            if a[i] > a[i + rng]:
                const = a[i]
                a[i] = a[i+rng]
                a[i + rng] = const
                flag = True
    return a