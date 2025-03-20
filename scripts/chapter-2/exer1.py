#  

def largest_odd(x, y, z): 
    answer = min(x,y,z)
    if x % 2 != 0 :
        answer = x 
    if y % 2 != 0 and y > answer:
        answer = y
    if z%2 != 0  and z > answer:
        answer = z 
    return answer  
        
    

def smallest_odd(numbers):
    
    answer = None 
    for num in numbers:
        if num % 2 == 1:
            if answer is None or num < answer:
                answer = num
    return answer
    
    
    
    
def find_max(numbers):
    answer = None 
    for num in numbers:
        if answer is None or num > answer:
            answer = num 
    return answer
    


    