#19
d = {}
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()
for line in file_content:
    line = line.split()
    name = line[0]
    if name in d:
        d[name] = d[name] + 1
    else:
        d[name] = 1
print(d)