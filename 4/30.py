#30
input_path = "neko.txt.mecab"
with open(input_path, "r") as f:
    file_content = f.readlines()
    
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

for line in file_content:
    line = line.split("\t")
    if len(line)>=2:
        word = mapping(line)
        #一個だけ実行
        break