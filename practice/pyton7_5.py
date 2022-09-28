
def a(n):
    if n==1:
        return 1
    else:
        return a(n-1)+2*n-1
print(a(2))
