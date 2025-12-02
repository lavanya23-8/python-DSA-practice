s = "mississippi"
freq = {}

for c in s:
    freq[c] = freq.get(c, 0) + 1

print(freq)
