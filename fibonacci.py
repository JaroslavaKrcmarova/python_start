# FOR FIBONACCI
# 0 1 1 2 3 5 8 13 21 34

def fibonacci():
    list=[0,1]
    for i in range(1,100):
        n = len(list)-1
        n_1= list[n]+list[n-1]
        list.append(n_1)
    return list

print(fibonacci())

# FOR FIBONACCI

def fibonacci2(list=[0,1]):
    n = len(list)-1
    n_1= list[n]+list[n-1]
    list.append(n_1)
    if list[n]<100:
        fibonacci2(list)
    return list

print(fibonacci2([0,1]))

def fibonacci3(number):
    if number == 1:
        return 0
    if number == 2:
        return 1
    else:
        return fibonacci3(number-1) + fibonacci3(number-2)

print(fibonacci3(8))