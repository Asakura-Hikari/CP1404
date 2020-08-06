"""example"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""a"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""b"""
for i in range(1, 20, 1):
    print(i, end=' ')
print()

"""c"""
for i in reversed(range(21)):
    print(i, end=' ')
print()

"""d"""
num = int(input("Number of Stars : "))
for i in range(num):
    print("*", end=' ')
print()

"""e"""
num = int(input("level of Stars : "))
for i in range(1, num+1):
    print("*" * i)
print()
