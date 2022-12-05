def readlines():
    f = open("in")
    return [int(lines.rstrip()) for lines in f]


lines = readlines()
current_sum = lines[0] + lines[1] + lines[2]
count = 0
for i in range(3, len(lines)):
    ss = lines[i] + lines[i - 1] + lines[i - 2]
    if ss > current_sum:
        count += 1
    current_sum = ss

print(count)
