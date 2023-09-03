text = input()

count = 0

for i in range(len(text) - 1, 0, -1):
    if text[i] == 'a':
        count += 1

print(count)