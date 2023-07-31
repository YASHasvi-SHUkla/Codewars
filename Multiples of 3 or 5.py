def solution(number):
    ls = []
    
    for i in range(2,number): # start from 2 coz we want multiples of 3 and 5
        
        if i%3 == 0 ^ i%5 == 0:  # checks if i is completely divide by 3 or 5 but not both(using XOR)
            ls.append(i)
            
        elif i%3 == 0 or i%5 == 0:
            ls.append(i)
            
    return sum(ls) # returning sum of ls
