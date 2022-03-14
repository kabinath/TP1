def multiple(n, p):
    """ Renvoie le produit de n par p """
    produit = 0
    while n != 0:
        if n % 2 == 1:      
            produit = produit + p
        n = n//2
        p = p + p
    return produit

#def multiple(a,b):
    A = a
    B = b
    S = 0
    while A != 0:
        if A%2 == 1:
            S = S+B
        A = A//2
        B = B+B
    return S

print("Saisir un premier entier : ", end="") 
a = int(input())
print("Saisir le Second entier : ", end="")
b = int(input())

y = multiple(a,b)
print("le résultat de : ", a, "*", b, "est : ", y)