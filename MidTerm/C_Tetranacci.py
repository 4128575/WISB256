n=int(input())

def tetranacci(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 0
    elif n==3:
        return 1
    else:
        return tetranacci(n-1)+tetranacci(n-2)+tetranacci(n-3)+tetranacci(n-4)
print(tetranacci(n))