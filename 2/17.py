#17
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()

Set = set()

for line in file_content:
    line = line.split()
    name = set(list(line[0]))
    Set = Set | name
print(Set)