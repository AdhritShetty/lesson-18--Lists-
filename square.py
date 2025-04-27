squarelist=[0,1,4,9,16,25,36,49,64,81]
print("There are the squares of numbers from 0 to 9")
sq=int(input("enter a number from 0-9 for the answer:"))
if sq<10:
    print(squarelist[sq])
elif sq<0:
    print("negative numbers are not in range")
else:
    print("you are out of range")
if sq%2==0:
    print("the square is even")
else:
    print("the square is odd")