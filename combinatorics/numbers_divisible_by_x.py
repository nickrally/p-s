# How many numbers between 1 and 100 (inclusive) are divisible by 5 or 8?

li = range(1,101) # [1...100]
x = 5
y = 8
divisible_by_x = []
divisible_by_y = []
for e in li:
    if e % x == 0 and e % y == 0:
        divisible_by_x.append(e)
        divisible_by_y.append(e)
    elif e % x == 0:
        divisible_by_x.append(e)
    elif e % y == 0:
        divisible_by_y.append(e)

print(len(divisible_by_x))
print(len(divisible_by_y))

intersect = set(divisible_by_x).intersection(set(divisible_by_y)) # {40, 80}
print (list(intersect))






