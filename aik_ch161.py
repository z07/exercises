import sys
n = int(sys.argv[1], 10)
if n > 100 or n < 3:
    print("error")
a_list = []
for i in range(2, 2+n):
    a_list.append(int(sys.argv[i]))

combinations = []
length_list = [0]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            edges = [a_list[i],a_list[j],a_list[k]]
            if sum(edges) - max(edges) > max(edges) and sum(edges) > max(length_list):
                answer = [sum(edges), edges]
                length_list.append(sum(edges))
if len(length_list) == 1:
    print 0
else:
    print answer




