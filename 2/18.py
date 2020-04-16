#18
d = {}
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()

for line in file_content:
    count = line.split()[2]
    line = line.split()
    if not(count in d):
        d[count] = []
        d[count].append([line[0], line[1], line[3]])
        continue
    d[count].append([line[0], line[1], line[3]])
sorted_d = sorted(d.items(), key=lambda x:x[0], reverse=True)

for element in sorted_d:
    key = element[0]
    for line in d[key]:
        print(line[0]+"\t"+line[1]+"\t"+key+"\t"+line[2])