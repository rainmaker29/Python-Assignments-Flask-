#Map
arr = [5,4,3,2,1]
def mymap(f,arr):
    new_arr=list()
    for x in arr:
        new_arr.append(f(x))
    return new_arr

#Filter
def myfilter(f,arr):
    new_arr=list()
    for x in arr:
        if f(x):
            new_arr.append(x)
    return new_arr

