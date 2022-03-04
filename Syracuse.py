n = int(input())
syracuse = [n]
while(n!=1) : 
    if(n%2 == 0) :
        n = n//2
        syracuse.append(n)
    elif(n%2 == 1) :
        n = n*3 + 1
        syracuse.append(n)

print(syracuse)