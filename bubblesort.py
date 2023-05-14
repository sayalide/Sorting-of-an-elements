def bubblesort(array1):
    p=len(array1)
    bstart_time = time.time()
    for i in range(len(array1)):
        array_sorted = True
        for j in range(len(array1) - i - 1):
            if array1[j]> array1[j+1]:
                array1[j],array1[j+1] = array1[j+1],array1[j]
                array_sorted = False
               
        if array_sorted:
            break
    bubblesorttime =time.time() - bstart_time
    return bubblesorttime




