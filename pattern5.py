"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""

for i in range(6,0,-1):
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()