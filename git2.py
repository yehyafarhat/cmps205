


# i was trying to produce this function using a for loop but that wont work because the function will not know when to stop, it will just looping in the range
# the while loop for this is superior
import sys
def longest(string,ind):#this function see the string in alphabetic order
    w=" "
    i=ind
    while(i< len(string)-1) and (string[i]<= string[i+1]):
        w=w+string[i]
        i=i+1
    w=w+string[i] #the reason we add the same line outside the loop is because in the the loop the range goes outside the index
    return(w)

def longest_substring(string):#this identifies the longest ordered line of characters
    a=" "
    for i in range(len(string)-1):
        p=longest(string,i)
        if len(p)>len(a):
            a=p
    return(a)


for i in range(1,len(sys.argv)):  # to take the string from the command line
    if longest_substring(sys.argv[1]):
        print("Longest substring in alphabatic order is:",longest_substring(sys.argv[1]))


