input_string = input().strip()

pair_count = {}

for i in range(len(input_string) - 1):
    pair = input_string[i:i+2]
    if pair in pair_count:
        pair_count[pair] += 1
    else:
        pair_count[pair] = 1

max_pairs = [pair for pair, count in pair_count.items() if count == max(pair_count.values())]

print(max(max_pairs))