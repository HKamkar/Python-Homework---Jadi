n=int(input())
L=[]

 
for i in range(n):
	L.append(input().split())
for i in range(len(L)):
	for j in range(2):
		L[i][j]=int(L[i][j])
   		
flag=0 
L.sort() 

for i in L:
	for j in range(1,len(L)):
		if((i[1]>=L[j][1]) and (i[0]<L[j][0])):
	   	 flag=1
	    
if flag==1:
	print("happy irsa")
else:
	print("poor irsa")