import time

def loop():
	x=0
	pics = input("Enter pics number: ")
	var = int(input("Enter the fraction to reduce: "))
	print("")
	print("=============================================================")
	
	begin1 = time.time()
	#reading Pics
	for x in range(0, pics):
		#time begins
		begin2 = time.time()
		x = str(x)
		path =  'C:\\Users\\sarim\\Desktop\\LargePics\\' + x + '.jpg'
		print("Making Picture...")
		src = makePicture(path)
		print("Getting Resolution...")
		width = getWidth(src)
		width = str(width)
		height = getHeight(src)
		height = str(height)
		#Printing Actual Resolution
		print("")
		print("Resolution: " + width + "x" + height)
		print("")
		destwidth = getWidth(src)/var
		destheight = getHeight(src)/var
		print("Making Canvas...")
		canvas = makeEmptyPicture(destwidth,destheight)
		print("Starting Work...")
		sourceX = 1
		for targetX in range(0,int(destwidth)):
			sourceY = 1
			for targetY in range(0,int(destheight)):
				color = getColor(getPixel(src,sourceX,sourceY))
				setColor(getPixel(canvas,targetX,targetY), color)
				sourceY= sourceY + var
			sourceX = sourceX + var

			
		#repaint(canvas)
		pic = canvas
		#Saving image
		print("Saving Image...")
		writePictureTo(pic, 'C:\\Users\\sarim\\Desktop\\Sized\\' + x +'.jpg')
		

		
		#Time Elapsed
		end2 = time.time()
		time_1 = round(end2 - begin2 , 2)
		if time_1 > 59:

			print(str(time_1/60) + " minutes")
		else:
			time_1 = str(time_1)
			print(time_1 + " seconds")
			print("Time elapsed in this picture: " + time_1)
			print("") 
			#Printing Total Time Elapsed
			end1 = time.time()
			print("Total time elapsed till now: ")
			total_time = round(end1 - begin1, 2)
	
			if total_time > 59:

				print(str(total_time/60) + " minutes")
			else:
				total_time = str(total_time)
				print(total_time + " seconds")
			#Mentioning number of pictures done
			str(x)
			print("Number of Pics done: " + str((int(x)+1))) 
			print("")
			print("----------------------------------------------------------------")
			# Loop ends here

	print("=========================================================")
	print("")
	end1 = time.time()
	print("Total time elapsed: ")
	totaltime = end1 - begin1

	if totaltime > 59:

		totaltime = str(round(totaltime/60,2))
		print(totaltime + " minutes")
	else:
		totaltime = round(totaltime,3)
		totaltime = str(totaltime)
		print(totaltime + " seconds")
	endSound = makeSound('C:\\Users\\sarim\\Desktop\\Resizer\\camera.wav')
	play(endSound)


		         

		 
		      
			  