def narcissistic( value ):
    # Code away
  
    s = 0
    l = len(str(value))
    n = value
  
    while(n > 0):
        r = n%10
        n = n//10
        s =  s + r**l
      
    if value == s:
        return True
    else:
        return False
