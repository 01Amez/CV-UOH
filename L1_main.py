import cv2
import numpy
import matplotlib

b=[1,2,3,'k']
a = [
    [1,2,3,'hello'],
    ['d', True]]

for item in a:
    for it in item:
        print(it)

print(type(a))
print(len(a[0]))
print(a[1][1])
print(a)


b = 2

if b>0:
    print('positive')
elif b<10:
    print("negative")
else:
    print()


names = ['name1', 'name2', 'name3']

for n in names:
    print(n)

# for i in range(len(names)):
#     print(names[i])

