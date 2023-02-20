A = [2,7,4,6,5]
i = A.index(max(A))
proverka=True
from random import randint
lst = []
i = int(input("Введите количесво элементов: "))
n = int(input("Для заполения массива случайными числа 1,для ручного ввода  2: "))
if n == 1:
    lst = [randint(1,20) for i in range(i)]
    print(lst)
    maxElem = max(lst)
    indexMax = lst.index(maxElem)
    index = indexMax+1
    for index in range(indexMax+1,len(lst)):
        if lst[index]%2==0:
            lst[index]="chet elem"
    index=0
    while index<len(lst):
        if lst[index]=="chet elem":
            lst.pop(index)
            ind=indexMax
        index=index+1
    print(lst)

else:
    for x in range(i):
        string = "Введите " +str(x+1)+" элемент списка: "
        lst.append(input(string))
    for x in lst:
        if not x.isnumeric():
            proverka=False
            print("В списке могут быть только числа")
            break
if proverka:
    listic = [int(x) for x in lst]
    print(listic)
    t = 0
    # find max value in list
    max_value = max(listic)

    # find index of max value in list
    max_index = listic.index(max_value)
    print( max_value, max_index)
    u = max_index +1
    while u < len(listic):
        if listic[u]%2==0:
            del listic[u]
        else:
            u +=1
    print(listic)



