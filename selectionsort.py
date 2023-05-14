def selectsort( array1 ):
    sstart_time = time.time()
    for m in range( len(array1) - 1 ):
        min_index = m
        for n in range( m + 1, len(array1) ):
            if array1[n] < array1[min_index] :
                min_index = n

        if min_index != m :
            key = array1[m]
            array1[m] = array1[min_index]
            array1[min_index] = key


    selectsorttime = time.time() - sstart_time
    return selectsorttime
    


