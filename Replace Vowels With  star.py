s = "Python programming is fun"
vowels = "aeiouAEIOU"

result = "".join("*" if ch in vowels else ch for ch in s)
print(result)
