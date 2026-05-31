def clean(name):
    left =0
    for right in range(1, len(name)):
        if name[right] != name[left]:
            left = left + 1
            name[left] = name[right]
    return left + 1




names = ['v', 'a', 'a', 'i', 'b', 'h', 'a', 'v']
count =clean(names)
print(names[:count])