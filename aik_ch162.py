import sys
L = int(sys.argv[1],10)
n = int(sys.argv[2],10)
x_list = []
for i in range(3,3+n):
    x_list.append(int(sys.argv[i]))

minT = 0
for i in range(n):
    minT = max(minT, min(x_list[i], L - x_list[i]))

maxT = 0
for i in range(n):
    maxT = max(maxT, max(x_list[i], L - x_list[i]))

print(str(minT) + "\n" + str(maxT))
