def mergesort(m):
    mstart_time = time.time()
    
    if len(m)>1:
        mid=int(len(m)//2)
        l=m[0:mid]
        r=m[mid:]

        mergesort(l)
        mergesort(r)

        t=0
        u=0
        v=0

        while t<len(l) and u<len(r):
            if l[t]<r[u]:
                m[v]= l[t]
                t=t+1
            else:
                m[v]=r[u]
                u=u+1
            v=v+1
        while t<len(l):
            m[v]=l[t]
            t=t+1
            v=v+1

        while u<len(r):
            m[v]=r[u]
            u=u+1
            v=v+1
            
    mergesorttime =time.time() - mstart_time
    return mergesorttime
