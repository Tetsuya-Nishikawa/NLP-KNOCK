#08
def cipher(s):
    str_code = ord(s)
    if ord("a")<=str_code and str_code<=ord("z"):
        return 219-str_code
    return s

print(cipher("a"))