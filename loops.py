for i in range(1,6):
    print('number',i)

count=1

while count<=5:
    print('count',count)
    count+=1

for i in range(1,10):
    if i==5:
        continue
    if i==8:
        break
    print(i)
else:
    print("loops succesfully")

#📈 range() function

# range(start, stop, step)
for i in range(2, 11, 2):   # 2, 4, 6, 8, 10
    print(i)
