a = 1
b = 2

scores = [3,4,5,6,a,b]

for x in scores:
    if x == 0:
        print('失格')
    elif x < 5:
        print('追試')
    else:
        print('合格')