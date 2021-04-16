
#666666
 #55555
 # 4444
  # 333
   # 22
    # 1
print("---------------pattern 1---------------")
x = int(input())
for i in range(x, 0, -1):
    for j in range(i, x):
        print(" ", end="")
    for k in range(0, i):
        print(i, end="")
    print("")


# 55555
# 4444
# 333
# 22
# 1

print("---------------pattern 2---------------")
x = int(input())
for i in range(x, 0, -1):
    for k in range(0, i):
        print(i, end="")
    for j in range(i, x):
        print(" ", end="")
    print("")

# 1
# 22
# 333
# 4444
# 55555

print("---------------pattern 3---------------")
x = int(input())
for i in range(0, x+1, 1):
    for k in range(0, i):
        print(i, end="")
    for j in range(i, x):
        print(" ", end="")
    print("")

# 1
# 12
# 123
# 1234
# 12345

print("---------------pattern 4---------------")
x= int (input())
for i in range(1, x+1):
    for k in range(1, i+1):
        print(k, end="")
    print("")


# 11111
# 2222
# 333
# 445

# 5

print("---------------pattern 5---------------")
x = int(input())
for i in range(1, x+1, 1):
    for k in range(i, x+1):
        print(i, end="")
    print("")

# 5
# 44
# 333
# 2222
# 11111

print("---------------pattern 6---------------")
x = int(input())
for i in range(x, 0, -1):
    for k in range(i, x+1):
        print(i, end="")
    print("")

# 5
# 45
# 345
# 2345
# 12345


print("---------------pattern 7---------------")
x = int(input())

for i in range(x, 0, -1):
    for k in range(i, x+1):
        print(k, end="")
    print("")

# 12345
# 2345
# 345
# 45
# 5
print("---------------pattern 8---------------")
x = int(input())
for i in range(1, x+1):
    for k in range(i, x+1):
        print(k, end="")
    print("")


# 1
# 21
# 321
# 4321
# 54321
print("---------------pattern 9---------------")
x = int(input())
for i in range(1, x+1):
    for k in range(i, 0, -1):
        print(k, end="")
    print("")


print("---------------pattern 10---------------")
x = int(input())
for i in range(x, 0, -1):
    for k in range(i, 0, -1):
        print(k, end="")
    print("")
