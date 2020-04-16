#13

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

merge = ""
output_path = "merge.txt"
col1_list = col1.split()
col2_list = col2.split()

for name, sex in zip(col1_list, col2_list):
    merge = merge + name + "\t" + sex + "\n"

with open(output_path, "w") as f:
    f.write(merge)