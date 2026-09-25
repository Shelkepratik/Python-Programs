number=[10,20,30,40,50,60]
target=40

left=0
right=len(number)-1 #6-1=5

while left<=right:  #0<5
    middle=(left+right)//2

    if number[middle]==target:
        print("Found at index: ",middle)
        break

    elif number[middle]<target:
        left=middle+1
    else:
        right=middle-1
else:
    print("Not Found")