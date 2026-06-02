with open("datasets/rosalind_fibd.txt") as f:
    data = f.read().strip().split(" ")

N, m = map(int, data)

b = [1]
a = [0]
t = [1]

for n in range(2, N + 1):

    if n <= m:
        a.append(a[-1] + b[-1])
    else:
        a.append((a[-1] + b[-1]) - b[-m])

    b.append(a[-2])
    t.append(b[-1] + a[-1])

print(t[-1])
