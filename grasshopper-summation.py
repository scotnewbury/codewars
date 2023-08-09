def summation(num):
    pass # Code here
    sum = 0
    while num > 0:
        sum = sum + num
        print (sum)
        num -= 1
    return (sum)
  
num = int(input("Pick a number: "))

print("The summation is " + str(summation(num)))
