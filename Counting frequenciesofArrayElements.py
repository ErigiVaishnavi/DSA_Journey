'''arr=[10, 20, 20, 10, 10, 20, 5, 20]
n=len(arr)
key=arr[0]
value=0

for i in range(0,n):
  if arr[i]==key:
    value+=1
  elif arr[i]!=key:
    key.append(arr[i])
print(key, value)'''


arr=[10, 20, 20, 10, 10, 20, 5, 20]
freq={}
for i in arr:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1

for key, value in freq.items():
    print(key, value)