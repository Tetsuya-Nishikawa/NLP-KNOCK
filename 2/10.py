#10
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()
print("ファイルの行数は、", len(file_content))