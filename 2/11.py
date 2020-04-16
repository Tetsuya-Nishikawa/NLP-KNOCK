#11
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.read()
print(file_content.replace("\t", " "))