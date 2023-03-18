inp = "3,2,6,5,1,4,8,9"
nums = inp.split(',')
num1=0
for i in nums:
	i = int(i)
	if i==5:
		break
	num1 += i
for j in nums[::-1]:
	j = int(j)
	if j==8:
		break
	num1 += j
num2=""
for k in range(inp.find('5'), inp.find('8')+1):
	if inp[k].isdigit():
		num2 += str(inp[k])

print(num1 + int(num2))
