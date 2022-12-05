f = open("in")
last = 100000
count = 0
for line in f:
    line = line.rstrip()
    num = int(line)
    if last < num:
        count += 1
    last = num

print(count)