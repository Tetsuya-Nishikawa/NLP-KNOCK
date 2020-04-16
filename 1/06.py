#06
def n_gram(S):
    return ["".join(S[i:i+2]) for i in range(0, len(S)-2+1, 1)]

X = set(n_gram(list("paraparaparadise")))
Y = set(n_gram(list("paragraph")))

union = X | Y
intersection = X & Y
difference = X-Y

print("union\n", union)
print("intersection\n", intersection)
print("difference\n", difference)