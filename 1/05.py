#05

def n_gram(S):
    return [S[i:i+2] for i in range(0, len(S)-2+1, 1)]

#単語bi-gram
n_gram("I am an NLPer".split())

#文字bi-gram
n_gram(list("".join("I am an NLPer".split())))