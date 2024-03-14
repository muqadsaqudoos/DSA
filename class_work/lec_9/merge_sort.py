def m_s(arr,p,r):
    if p<r:
        q = (p+r)//2
        m_s(arr,p,q)
        m_s(arr,q+1,r)
        merge(arr,p,q,r)
    return arr

def merge(arr,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = arr[p+i]

    for i in range(n2):
        R[i] = arr[q+i+1]

    i = j = 0
    k = p
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while i <n1:
        arr[k] = L[i]
        i+=1
        k+=1
    while j <n2:
        arr[k] = R[j]
        j+=1
        k+=1
    return arr



a = [9,0,4,3,15,11,5,2,8,3,9,1,100,-1]
print(m_s(a,0,len(a)-1))
    
