#09
import random
S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
S = S.split()

result = []

for s in S:
    if len(s)>4:
        s_list = list(s)
        top = s_list[0]
        last = s_list[len(s)-1]
        middle = s_list[1:len(s)-1]
        random.shuffle(middle)
        result.append(top+"".join(middle)+last)
        continue
    result.append(s)