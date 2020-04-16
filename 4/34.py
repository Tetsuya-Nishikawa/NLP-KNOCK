#34
import MeCab as mecab 


text = []
input_path = "neko.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()
    
for line in file_content:
    line = line.replace("\u3000", "").replace("\n", "")
    text.append(line)
m = mecab.Tagger()

d = {}

def extract_noun(sentence):
    sentence_info = m.parse(sentence).split("\n")
    sentence_info.remove("EOS")
    sentence_info.remove("")

    print(sentence_info)
    for index in range(0, len(sentence_info)-1, 1):
        word_info1 = sentence_info[index]
        word_info2 = sentence_info[index+1]
        
        word1 = word_info1.split("\t")[0]
        word2 = word_info2.split("\t")[0]

        pos1   = word_info1.split("\t")[1].split(",")[0]
        pos2   = word_info2.split("\t")[1].split(",")[0]

        if pos1=="名詞" and pos2=="名詞":
            if len(word1+word2) in d:
                d[len(word1+word2)].append(word1+word2)
            else:
                d[len(word1+word2)] = []
                d[len(word1+word2)].append(word1+word2)
            
for line in text:
    extract_noun(line)