def solution(banana_list):
    def can_thumb_wrestle(a, b):
        return (a + b) % 2 == 0 and (a - b) % 2 == 0
    
    matched = [False] * len(banana_list)
    trainers_left = len(banana_list)
    
    if len(banana_list)==2 and can_thumb_wrestle(banana_list[0], banana_list[1]):
        return 2
    
    for i in range(len(banana_list)):
        if not matched[i]:
            for j in range(len(banana_list)):
                if not matched[j] and can_thumb_wrestle(banana_list[i], banana_list[j]) and i!=j:
                    matched[j] = True
                    matched[i] = True
                    trainers_left -= 2  
                    break
    return trainers_left
