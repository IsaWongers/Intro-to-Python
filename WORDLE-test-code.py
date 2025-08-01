values = [1,2,3,4]
inOrder = True
previous = values[0]
i = 1

while i < len(values) and inOrder == True:
    if previous < i:
        inOrder = True
        previous = i
    else:
        inOrder = False
    i += 1

if inOrder:
    print("the values are in order")
else:
    print("the values are not in order")
