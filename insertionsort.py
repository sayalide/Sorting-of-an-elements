def insertionsort(array1):
    istart_time = time.time()
    
    for m in range(1, len(array1)):
        temp = array1[m]
        n = m - 1
        
        while n >= 0 and temp < array1[n] :
            array1[n + 1] = array1[n]
            n = n - 1
        array1[n + 1] = temp
    
    insertsorttime =time.time() - istart_time
    return insertsorttime




