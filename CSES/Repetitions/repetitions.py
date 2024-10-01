line = input()

start, end = 0, 1
longest = 1

while end < len(line):
    if line[start] == line[end]:
        longest = max(longest, end-start+1)
    else:
        start = end
    end += 1

print(longest)