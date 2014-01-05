import sys
n = int(sys.argv[1],10)
if n > 50 or n < 1:
    print("error")
m = int(sys.argv[2],10)
if m > 10**8 or m < 1:
    print("error")
k_list = []
for i in range(3,3+n):
    k_list.append(int(sys.argv[i],10))
sum_list = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                sum_list.append(k_list[i] + k_list[j] + k_list[k] + k_list[l])

if m in sum_list:
    print("YES")
else:
    print("NO")
