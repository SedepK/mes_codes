def difference ():
    import random as d 
    m = [d.randint (10, 47) for i in range (57)]
    difference = [m [i +1] - m[i] for i in range (len (m) -1)]
    return(difference)
print (difference())
