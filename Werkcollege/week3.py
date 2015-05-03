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

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if not isinstance(word, str):
        print(word, 'is not a string.')
        return None
    elif len(word)==1:
        return True
    elif len(word)==2 and first(word)==last(word):
        return True
    elif first(word)==last(word):
        return is_palindrome(middle(word))
    else:
        print(word, 'is not a palindrome.')
        return None

def gcd(a, b):
    if not isinstance(a, int):
        print('gcd is only defined for natural numbers.')
        return None
    if not isinstance(b, int):
        print('gcd is only defined for natural numbers.')
        return None
    if a<0:
        print('gcd is only defined for natural numbers.')
        return None
    if b<0:
        print('gcd is only defined for natural numbers.')
        return None
    if a==b:
        return a
    if a>b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)