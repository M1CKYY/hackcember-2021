count = 0
list = []
with open("rockyou.txt", "r", encoding="Latin-1") as f:
    for line in f:
        count += 1
        if len(line) == 97:
            print(count)
            print(line)
            list.append(line)
print(list)
