def pascal(n):
    row = []
    for k in range(n):
        row = [1 if i == 0 or i == k else row[i-1] + row[i] for i in range(k+1)]
        yield row

n = 5
for row in pascal(n):
    print(' '.join(map(str, row)).center(n * 2) + '\n')



