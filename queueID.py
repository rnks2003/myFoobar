def solution(start,length):
    def rXor(start,end):
        def Xor(end):
            res=0
            if end%4 == 0:
                res =end
            elif end%4 == 1:
                res = 1
            elif end%4 ==2:
                res = end+1
            return res
        return Xor(end)^Xor(start-1)
    
    temp = start
    res = 0
    j = 0
    
    for i in range(length,0,-1):
        end = temp + i-1
        res^=rXor(temp,end)
        j+=1
        temp = end+j
    return res
