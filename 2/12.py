#12
col1 = ""
col2 = ""
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()

for line in file_content:
    name = line.split()[0]
    sex    = line.split()[1]
    col1 = col1 + name + "\n"
    col2 = col2 + sex    + "\n"
print(col1)