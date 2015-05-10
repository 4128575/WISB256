def square_root(a):
    x=a+0.01
    while True:
        epsilon=0.000000000001
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            print(y)
            break
        x=y
square_root(13)