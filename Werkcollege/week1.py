import urllib.request
def check_fermat(a, b, c, n):
    if n>2 and a**n+b**n==c**n:
        print('Hole smokes, Fermat was wrong!')
    else:
        print('No, that does not work.')
def inputfermat():
    x=int(input('What is a? '))
    y=int(input('What is b? '))
    z=int(input('What is c? '))
    m=int(input('What is n? '))
    check_fermat(x,y,z,m)

zipcode = '02492'
url = 'http://uszip.com/zip/' + zipcode
conn2= urllib.request.urlopen(url)

for line in conn2.fp:
    line = line.strip()
    lineStr = str(line, encoding='utf8')
    if 'Total population' in lineStr:
        print(lineStr)
#    if 'Longitude' in line: 
#        print(line)
#    if 'Latitude' in line: 
#        print(line)

conn2.close()