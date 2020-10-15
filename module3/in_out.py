# with open("sample.txt") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)

with open("sample.txt") as file:
    for line in file:
        line = line.strip()
        print(line)

with open("out.txt", "w") as out:
    out.write("Hello\n")
