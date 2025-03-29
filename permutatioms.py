def permute(string, step=0):
    if step == len(string):
        print("".join(string))
    for i in range(step, len(string)):
        string_copy = [c for c in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permute(string_copy, step + 1)

string = "abc"
permute(list(string))
