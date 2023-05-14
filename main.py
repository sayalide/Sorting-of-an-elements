import time
import numpy as np
import pprint

exec(open("./mergesort.py").read())
exec(open("./bubblesort.py").read())
exec(open("./quicksort.py").read())
exec(open("./selectionsort.py").read())
exec(open("./insertionsort.py").read())
exec(open("./heapsort.py").read())
value=[]
value1=[]
value2=[]
value3=[]
value4=[]
value5=[]
value6=[]

m=int(input('Enter 1: Enter 1 to provide inputs to array: '))
if m==1:
    m=int(input('Enter the length of array and enter to provide elements: '))
    for i in range(0,m):
        n= int(input())
        value.append(n)
        value1.append(n)
        value2.append(n)
        value3.append(n)
        value4.append(n)
        value5.append(n)
        value6.append(n)
               
else:
    print('You have not enter valid input')
mergesorttime=mergesort(value1)
print('sorted list obtained by merge sort ')
print(value1)
bubblesorttime=bubblesort(value2)
print('sorted list obtained by bubble sort ')
print(value2)
size = quick()
for m in value3:
    size.insert(m)
quicksorttime=size.quicksort()
print('sorted list obtained by Quick sort ')
size.pprint()
selectsorttime=selectsort(value4)
print('sorted list obtained by selection sort ')
print(value4)
insertsorttime=insertionsort(value5)
print('sorted list obtained by insertion sort ')
print(value5)
heapsorttime=heapsort(value6)
print('sorted list obtained by heap sort ')
print(value6)

print ('Mergesort running time obtained in seconds is : %s' %mergesorttime)
print ('Bubblesort running time obtained in seconds is: %s' %bubblesorttime)
print ('Quicksort running time obtained in seconds is: %s' %quicksorttime)
print ('Selectionsort running time obtained in seconds is: %s' %selectsorttime)
print ('Insertionsort running time obtained in seconds is: %s' %insertsorttime)
print ('Heapsort running time obtained in seconds is: %s' %heapsorttime)
print('')

u=[]
u.append(mergesorttime)
u.append(bubblesorttime)
u.append(quicksorttime)
u.append(selectsorttime)
u.append(insertsorttime)
u.append(heapsorttime)












