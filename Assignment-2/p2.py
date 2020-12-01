from collections import deque
arr=[5,4,3,2,1]
de=deque(arr)
for i in range(5):
    de.rotate(1)
    for j in de:
        print(j,end=" ")
    print("")

