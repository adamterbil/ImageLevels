from PIL import Image

#open an image

picture = Image.open("underwater2.jpg") 
#picture.show()

###size

w, h = picture.size
##print("The width is " + str(w) + " pixels")
##print("The height is " + str(h) + " pixels")
##
###pixel = picture.getpixel((0,0))[0]
###print(pixel) 
##
##extremes = picture.getextrema()
##print(extremes)
##print("Since this picture is black and white the maximum values are " +
##      str(extremes[0][1]) + ", " + str(extremes[1][1]) + ", " +
##      str(extremes[2][1]))
##
##
###mean pixel value
##
##total = 0
##for i in range(0, w):
##    for j in range(0, h):
##        total += picture.getpixel((i,j))[0]
##
##mean = total / (w*h)
##print("The mean pixel value is " + str(mean))
##
### (e)
##
##for i in range(0,w):
##    for j in range(0,h):
##        if(picture.getpixel((i,j))[0] < mean):
##            picture.putpixel((i,j), (0,0,0))
##        else:
##            picture.putpixel((i,j), (255,255,255))
##
##picture.show() 

##Image Interpolation

##newPicture = picture.resize((320, 216), Image.NEAREST)
##newPicture.save("underwater2resized.jpg") 
##newPicture.show() 
##print(newPicture.size)
##
##newPicture2 = newPicture.resize((640,432), Image.BILINEAR)
##newPicture2 = newPicture2.resize((640, 432), Image.BICUBIC)
##newPicture2.save("underwater2resized2.jpg")
##newPicture2.show()
##print(newPicture2.size)

##Reducing Gray Levels


##Loop 7 times, integer divide by 2 each time

for x in range(1,8): 
    for i in range(0, w):
        for j in range(0,h):
            a = picture.getpixel((i,j))[0]
            b = picture.getpixel((i,j))[1]
            c = picture.getpixel((i,j))[2] 
            picture.putpixel((i,j), (a - (a % (2**x)), b - (b % (2 ** x)), c - (c % (2 ** x))))

    picture.show()

