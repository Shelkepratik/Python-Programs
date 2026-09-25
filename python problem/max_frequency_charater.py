text=input("Enter the string: ")
frequency={}  #create dictonary
for ch in text:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
print(frequency)
max_char=""
max_count=0
for ch in frequency:
    if frequency[ch]>max_count:
        max_count=frequency[ch]
        max_char=ch
print("Maximum frequency character:",max_char)
print("frequency:",max_count)