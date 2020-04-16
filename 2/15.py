#15
def print_head(file, N):
    file = file[::-1]
    for line in file[0:N]:
        print(line)
input_path = "popular-names.txt"
with open(input_path, "r") as f:
    file_content = f.readlines()

print_head(file_content, 100)