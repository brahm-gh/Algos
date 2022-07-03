from datetime import datetime
import timeit

with open('Vibrio_cholerae.txt', 'r') as f:
    t = f.read()

with open('ori.txt', 'r') as f:
    p = f.read()


def find_boyer_moore(Text, Pattern):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(Text), len(Pattern)  # introduce convenient notations
    if m == 0:  # trivial search for empty string
        return 0
    last = {}  # build ’last’ dictionary
    for k in range(m):
        last[Pattern[k]] = k  # later occurrence overwrites
        # align end of pattern at index m-1 of text
    i = m - 1  # an index into T
    k = m - 1  # an index into P
    while i < n:
        if Text[i] == Pattern[k]:  # a matching character
            if k == 0:
                return i  # pattern begins at index i of text
            else:
                i -= 1  # examine previous character
                k -= 1  # of both T and P
        else:
            j = last.get(Text[i], -1)  # last(T[i]) is -1 if not found
            i += m - min(k, j + 1)  # case analysis for jump step
            k = m - 1  # restart at end of pattern
    return -1


start = datetime.now()
print(find_boyer_moore(t, p))
end = datetime.now()
duration = end - start
print(f'It took {duration} to run the algorithm')
