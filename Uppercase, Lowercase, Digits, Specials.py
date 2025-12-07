s = "Hello123@Python!"

upper = lower = digits = special = 0

for ch in s:
    if ch.isupper(): upper += 1
    elif ch.islower(): lower += 1
    elif ch.isdigit(): digits += 1
    else: special += 1

print("Upper:", upper)
print("Lower:", lower)
print("Digits:", digits)
print("Special:", special)
