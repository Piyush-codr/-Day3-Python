'''#list comprehension



#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)
    


#list comprehension
print([i for i in range(11)])


#for loop version--odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2!=0])

result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])'''

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop odd square it or if even square
result=[]
for i in mat:
    i=[]
    for j in i:
        if j%2==0:
            result.append(j**2)
            result.append(j)
        else:
            result.append(j**3)
            result.append(j)
print(result)

#by using list comp

print([ele**3 if ele%2!=0 else ele**2 for i in mat for ele in i])










