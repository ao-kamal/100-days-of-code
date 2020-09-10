def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    print(d)


histogram('brontosaurus')

# TODO: ask on twitter "How would you rewrite this program more concisely using the 'get' method?"
