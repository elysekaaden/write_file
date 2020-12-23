data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼

num = int(input('Please enter random number: '))
data.append(num)
print(num)
print(data)
print(data[0])
print(data[1])

with open('test.csv', 'w') as f:
	f.write(
		str(data[0]) + '\n' + 
		str(data[1]) + '\n' + 
		str(data[2]) + '\n' + 
		str(data[3]) + '\n' +
		str(data[4]) + '\n'
		)
