import time
import random as rng
import sys 
import matplotlib.pyplot as plt 

exec(open("./mergesort.py").read())
exec(open("./bubblesort.py").read())
exec(open("./quicksort.py").read())
exec(open("./selectionsort.py").read())
exec(open("./heapsort.py").read())
exec(open("./insertionsort.py").read())
x=int(input('Enter the number for iterations :'))
n=8
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]

data=[]
for p in range(x):
        value1=[]
        value2=[]
        value3=[]
        value4=[]
        value5=[]
        value6=[]
        for q in range(0,n):
                a=rng.randint(-n,n)
                value1.append(a)
                value2.append(a)
                value3.append(a)
                value4.append(a)
                value5.append(a)
                value6.append(a)
        mergesorttime=mergesort(value1)
        bubblesorttime=bubblesort(value2)
        a = quick()
        for q in value3:
            a.insert(q)
        quicksorttime=a.quicksort()
        insertsorttime=insertionsort(value4)
        heapsorttime=heapsort(value5)
        selectsorttime=selectsort(value6)
        s1.append(mergesorttime)
        s2.append(bubblesorttime)
        s3.append(quicksorttime)
        s4.append(insertsorttime)
        s5.append(heapsorttime)
        s6.append(selectsorttime)
        data.append(n)
        n=n*3
print(data)
plt.plot(data,s1, label = "Merge Sort")
plt.plot(data,s2, label = "Bubble Sort")
plt.plot(data,s3, label = "Quick Sort")
plt.plot(data,s4, label = "Insertion Sort")
plt.plot(data,s5, label = "Heap Sort")
plt.plot(data,s6, label = "Selection Sort")
plt.xlabel('Input size taken for sorting')
plt.ylabel('Time taken by sorting algorithm in seconds')
plt.legend() 

plt.show()




