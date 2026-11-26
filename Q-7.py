s = input("Enter a string: ")
d = a = sp = 0
for ch in s:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        a += 1
    else:
        sp += 1
print("Digits:", d)
print("Alphabets:", a)
print("Special:", sp)