def sockMerchant(n, ar):
    # Write your code here
    ar=sorted(ar)
    set_elm =set(ar)
    aa =list(set_elm)
   
    c=[]
    for i in range(len(aa)):
        c.append(ar.count(aa[i]))

    
    cres=[i//2  for i in c]
    return sum(cres)
        
