def fibonacci(n):
    """
    This function make Fibonacci number fibonacci(int) == int!
    """
    nth = 0
    ath =[]
    for i in range(n+1):
        if i == 0:
            nth = 0
            ath.append(nth)
        elif i == 1:
            nth = 1
            ath.append(nth)
        elif i > 1 :
            nth =ath[len(ath)-1] + ath[len(ath)-2]
            ath.append(nth)
    return nth    
# print(fibonacci(8))

def lucas(n):
    """
    This function make Lucas number lucas(int) 
    """
    
    if n < 0:
        return('Please enter 0 or higher')
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return(lucas(n-1)+lucas(n-2)) 
# print(lucas(5))

def sum_series(n,n1=0,n2=1):
    """
    This function show the fibonacci & lucas sum methode ,Have one required parameter and two optional parameters, The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.
    """
    if n == 0:
        return n1
    elif n == 1:
        return n2
    else:
        return(sum_series(n-1,n1,n2)+sum_series(n-2,n1,n2))

# print(sum_series(8,7,6))

