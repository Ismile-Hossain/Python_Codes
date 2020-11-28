x=10
while x>0:
    print("{}".format(x))
    x-=1
print("While Loop!!")

#exercise "break" statement
qs=["What is your name? ","How old are you? ","what is your hieght? "]
n=0
while True:
    print("Print q to quit")
    a=input(qs[n])
    if a=="q":
        break
    n=(n+1)%3 #circular rotation

# #exercise "continue" statement
for i in range(1,5):
    if i==3:
        continue
    print(i)

