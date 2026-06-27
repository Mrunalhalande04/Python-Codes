Arr=[1,2,3,4]
Brr=[4,5,6,7]

Result=[]

for i in range(len(Arr)):
   if Arr[i] not in Result:
      Result.append(Arr[i])


for j in range(len(Brr)):
   if Brr[j] not in Result:
      Result.append(Brr[j])


for item in Result:
   print(item)