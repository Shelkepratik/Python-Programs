str1=input("Enter the first string: ")
str2=input("Enter the second string; ")

frequency1={}
frequency2={}

for ch in str1:
    if ch in frequency1:
        frequency1[ch]+=1
    else:
        frequency1[ch]=1
for ch in frequency2:
    if ch in frequency2:
        frequency2[ch]+=1
    else:
        frequency2[ch]=1
if frequency1==frequency2:
    print("Anagram")
else:
    print("not anagram")