import os
path = input("Enter path of folder: ")
if len(path) < 3:
	print("Enter valid path..!!")
else:	
	os.chdir(path)
	print("Working Directory: ",os.getcwd())
	#---------------------------
	# leng = len(os.listdir())
	# for d in range(leng):
	# 	print(os.listdir()[d])
	#----------------------------
	print("Are You Sure To Rename All Files In This Folder..!!")
	inp = input().lower()
	if inp == 'yes' or inp == 'y':
		files = os.listdir()
		x = str(00)
		for file in files:
			y =str(x) + ".jpg"
			# print(type(x))
			os.rename(file, y)
			x = int(x)
			print("Done:", x)

			# print(type(x))
			x += 1
		print("Total files renamed:", x)
	else:
		pass
		print("Quitting...")




	
