num = 153
order = len(str(num))
temp = num;
sum = 0
while(temp>0):
	digit =temp%10
	sum += digit **order
	temp = temp//10
if(sum==num):
	print("Armstrong Number")
else:
	print("Not an Armstrong Number")