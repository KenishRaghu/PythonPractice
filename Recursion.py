def show(n):
    if (n == 0): # Always have a base case
        return
    print(n)
    show(n-1)
show(5)