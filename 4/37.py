#37
import matplotlib.pyplot as plt

sentences = []
sentence  = []
input_path = "neko.txt.mecab"
d = {}

with open(input_path, "r") as f:
    file_content = f.readlines()

def mode(file):
    for line in file:
        line = line[1].split()
        if "猫" in line:
            line.remove("猫")
            for word in line:
                if word in d:
                    d[word] += 1
                    continue
                d[word] = 1
        
def mapping(line):
    surface = 0
    fmt = line[1].replace("\n", "").split(",")
    base = 6
    pos = 0
    pos1 = 1
    word = {}
    word["surface"]=line[surface]
    word["base"]=fmt[base]
    word["pos"]=fmt[pos]
    word["pos1"]=fmt[pos1]
    return word
stream = ""

for line in file_content:
    line = line.split("\t")
    if len(line)>=2:
        word = mapping(line)
        if word["surface"]=="\u3000":
            continue
        stream = stream + " " + word["surface"]
        sentence.append(word)
        if word["surface"]=="。":
            sentences.append([sentence, stream])
            b = sentence
            stream = ""
            sentence = []
            continue

mode(sentences)
sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)


l = sorted_d[0:10]

x = []
y = []

for e in l:
    x.append(e[0])
    y.append(e[1])
plt.figure(figsize=(10,10))
plt.bar(x, y)