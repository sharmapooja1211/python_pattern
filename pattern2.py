"""
*
* *
* * *
* * * *
* * * * *

"""

for i in range(1,6):
    for j in range(1, i+1):
        print("* ",end="")
    print()


#  Another solution to do same pattern
# for i in range(1,6):
#     for j in range(1,6):
#         if i == j:
#             print(i  *  "*")