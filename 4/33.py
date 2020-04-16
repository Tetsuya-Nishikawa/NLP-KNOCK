#33
import MeCab as mecab

sentences = []
sentence  = []
input_path = "neko.txt.mecab"
with open(input_path, "r") as f:
    file_content = f.readlines()
m = mecab.Tagger()

def extract_noun(sentence):
    sentence_info = m.parse(sentence).split("\n")
    result = []
    for index in range(0, len(sentence_info)-2, 1):
        word_info1 = sentence_info[index]
        word_info2 = sentence_info[index+1]
        word_info3 = sentence_info[index+2]
        
        word1 = word_info1.split("\t")[0]
        word2 = word_info2.split("\t")[0]
        word3 = word_info3.split("\t")[0]
        pos1   = word_info1.split("\t")[1].split(",")[0]
        pos2   = word_info2.split("\t")[1].split(",")[0]
        pos3   = word_info3.split("\t")[1].split(",")[0]
        if pos1=="名詞" and word2=="の" and pos2=="名詞":
            result.append(word1+word2+word3)
            
    return result

for line in file_content