#input [-2,1,-3,4,-1,2,1,-5,4]
#output 6


number=[-2,1,-3,4,-1,2,1,-5,4]
current_sum=number[0]
maximum_sum=number[0]

for num in number[1:]:
    current_sum=max(num,current_sum+num)
    maximum_sum=max(maximum_sum,current_sum)
print("Maximum subarray sum: ",maximum_sum)