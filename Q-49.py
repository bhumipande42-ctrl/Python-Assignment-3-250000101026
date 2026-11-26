t = (1, 2, 3)
# t[0] = 99  # Error - tuples are immutable
t2 = t + (4,)
print("Original:", t)
print("Modified:", t2)