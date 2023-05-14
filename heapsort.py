def heap(array1,p,q):
    a = array1
    max_heap=q;
    left_a=2*q+1
    right_a=2*q+2
    if left_a <p and a[q] <a[left_a]:
        max_heap=left_a

    if right_a <p and a[max_heap] < a[right_a]:
        max_heap=right_a

    if max_heap !=q:
        a[q] , a[max_heap]= a[max_heap],a[q]
        heap(a,p,max_heap)

def heapsort(a):
    hstart_time = time.time()
    p=len(a)
    for q in range(p,-1,-1):
        heap(a,p,q)

    for q in range(p-1,0,-1):
        a[q],a[0]=a[0],a[q]
        heap(a,q,0)

    heapsorttime =time.time() - hstart_time
    return heapsorttime
