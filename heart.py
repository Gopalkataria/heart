## program to print a heart 
## the below variables to determine the size and shape of the heart 
# number of lines  l  to print 
l = 31
# characters to print 
char = "█"
emptychar = " "
# correction parameters of the heart equations 
k = l/6 
a = 0.2 
b = 0.5


# function which returns a charcter based on input characters 
def func(x, y, l):
    # below is equation of heart from internet , a and b and correction coefficients 
    # k largely determines the size 
    if (  (((a* x * x) + (b* y * y) - (k*k*k)) ** 3 ) < ( k * x*x*y*y*y)  ):
        return str(char)
    else:
        return str(emptychar) 

# storing the graph in array then printing out 
graph = [[func(x, y, l) for x in range(-l*2 , 2*l, 1)] for y in range(l, -l, -1)]
for line in graph:
    print("".join(line))
