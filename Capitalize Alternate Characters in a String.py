s = "programming"
result = ""

for i, ch in enumerate(s):
    result += ch.upper() if i % 2 == 0 else ch.lower()

print(result)
