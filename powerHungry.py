def solution(xs):
    n = len(xs)
    while xs.count(0)!=0:
        xs.remove(0)
        
    if len(xs)==0:
        return str(0)
    if len(xs)==1:
        if n==1: 
            return str(xs[0])
        else:
            return str(0)
       
    mul =1   
    max_neg=-1001
    for i in xs:
        mul*=i
        if i<0 and i>max_neg: max_neg = i
    if mul<0:
        mul=mul//max_neg
    return str(mul)
