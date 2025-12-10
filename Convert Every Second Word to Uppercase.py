s = "python makes learning easy"
words = s.split()

for i in range(len(words)):
    if i % 2 == 1:
        words[i] = words[i].upper()

print(" ".join(words))
