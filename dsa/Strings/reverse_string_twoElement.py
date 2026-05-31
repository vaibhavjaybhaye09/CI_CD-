# arr = [1, 2, 3, 4, 5, 6]
num = 'vaibhav'
arr = list(num)


def arr_rev(arr):

    m = 0
    c = len(arr)-1

    while m <= c:
        arr[m], arr[c] =  arr[c], arr [m]
        m+=1
        c-=1
    return "".join(arr)

print(arr_rev(arr))