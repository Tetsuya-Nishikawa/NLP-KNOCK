#04
S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
S = S.replace(".", "").split()
d = {}

index = [0, 4, 5, 6, 7, 8, 14, 15, 18]

for s in range(len(S)):
    if s in index:
        d[S[s][0]] = s + 1
        continue
    d[S[s][0:2]] = s + 1
print(d)