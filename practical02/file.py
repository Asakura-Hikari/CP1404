out_file = open("name.txt", 'w')
print("You name is Bob", file=out_file)
out_file.close()

out_file = open("numbers.txt", 'w')
print("17", file=out_file)
print("42", file=out_file)
print("400", file=out_file)
out_file.close()

read_file = open("numbers.txt", 'r')
number = 0
content = read_file.readlines()
print(type(content))

# for i in (0, 2):
#     number += int(read_file.readline())
# print(number)

read_file.seek(0)
for line in read_file.readlines():
    line = line.strip()
    print(line)

read_file.close()
