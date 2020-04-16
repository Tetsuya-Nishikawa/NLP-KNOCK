#03
S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
S = S.replace(",", "").replace(".", "")
S = S.split()

table = []

for s in S:
    table.append(len(s))
print(table)