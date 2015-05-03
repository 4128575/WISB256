def ack(m, n):
    if not isinstance(n, int):
        print('Ackermann is only defined for integers.')
        return None
    elif not isinstance(m, int):
        print('Ackermann is only defined for integers.')
        return None
    elif n<0:
        print('Ackermann is not defined for negative integers.')
        return None
    elif m<0:
        print('Ackermann is not defined for negative integers.')
        return None
    elif m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1, 1)
    elif m>0 and n>0:
        return ack(m-1, ack(m, n-1))
print(ack(3,4))