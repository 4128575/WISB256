import math

vuurkracht = int(input())
zwaartekracht = int(input())
afstand = int(input())
waarde=(afstand*zwaartekracht)/(vuurkracht*vuurkracht)
hoek = (1/2)*math.asin(waarde)
hoek ="{0:.2f}".format(hoek)
print(hoek)