import time

file = open('prime.dat', 'w')

limiet = int(input('Bovenlimiet? '))

T1 = time.perf_counter()

lijst = [1] * limiet
lijst2 = []
for i in range(2, int((limiet+1)/2)+1):
    for k in range(2, int(limiet/i)+1):
        lijst[k*i-1] = 0
for j in range(2, limiet):
    if lijst[j-1] == 1:
        lijst2.append(j)

T2 = time.perf_counter()

for item in lijst2:
  file.write("%s\n" % item)

file.close()

print('Found', len(lijst2), 'Prime numbers smaller than', limiet, 'in',  T2 - T1, 'sec.')