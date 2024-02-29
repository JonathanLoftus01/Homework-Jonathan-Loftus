# import torch

# torch.cuda.is_available()

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from matplotlib import cbook
from PIL import Image
from PIL import Image, ImageChops
import os 

image_path = "C:\\Users\\jonat\\Documents\\CODE lancashire\\Python CODE LANCS\\python homework\\leaf siloetes\\data\\data"
outline_path = "C:\\Users\\jonat\\Documents\\CODE lancashire\\Python CODE LANCS\\python homework\\leaf siloetes\\data\\outlines"


n=0
genus_species= os.listdir(image_path) # collection of species names sting
image_path2=image_path + "\\" + genus_species[85]
IndImage = os.listdir(image_path2)

print(image_path2 + "\\" + IndImage[2])
image = Image.open(image_path2 + "\\" + IndImage[2])
plt.imshow(image)
plt.show() # image 1


image.putpixel([200,200], 0)

plt.imshow(image)
plt.show() # image 1
 
width, height = image.size
print(width,height)
def surrounding_pixels(x,y, img, reach=1, location=False):
    width, height = img.size
    
    zero = x, y-reach
    one = x+reach, y-reach
    two = x+reach, y
    three = x+reach, y+reach
    four = x, y+reach
    five = x-reach, y+reach
    six = x-reach, y
    seven = x-reach, y-reach

    # sur_loc_pixels = [zero,one,two,three,four,five,six,seven]
    sur_loc_pixels = [zero,two,four,six,one,three,five,seven]
    # print(width, height)
    sur_loc_pixels = [list(coords) for coords in sur_loc_pixels]
    # print(sur_loc_pixels)
    # print(sur_loc_pixels[1][0])
    # print(type(sur_loc_pixels))
    for locs in range(len(sur_loc_pixels)):
        if 0 > sur_loc_pixels[locs][0]:
            sur_loc_pixels[locs][0] = 1
        elif sur_loc_pixels[locs][0] > width-1:
            sur_loc_pixels[locs][0] = width-2

        if 0 > sur_loc_pixels[locs][1]:
            sur_loc_pixels[locs][1] = 1
        elif sur_loc_pixels[locs][1] > height-1:
            # print(sur_loc_pixels[locs][1], height)
            sur_loc_pixels[locs][1] = height-2
    
    sur_loc_pixels = [tuple(coords) for coords in sur_loc_pixels]
    # print(sur_loc_pixels)
    # zero,one,two,three,four,five,six,seven = sur_loc_pixels
    zero,two,four,six,one,three,five,seven = sur_loc_pixels
    
    #the below values convert the surrounding pixel locations to values at the locations           
    zeroV = img.getpixel((zero))
    oneV = img.getpixel((one))
    twoV = img.getpixel((two))
    threeV = img.getpixel((three))
    fourV = img.getpixel((four))
    fiveV = img.getpixel((five))
    sixV = img.getpixel((six))
    sevenV = img.getpixel((seven))

    # sur_loc_pixels = [zero,one,two,three,four,five,six,seven]
    # sur_pixels = [zeroV,oneV,twoV,threeV,fourV,fiveV,sixV,sevenV]
    sur_pixels = [zeroV,twoV,fourV,sixV,oneV,threeV,fiveV,sevenV]
    if location == False:
        return sur_pixels 
    elif location == True:
        return sur_loc_pixels




Boundary_array=[]

for y in range(height-1):
    for x in range(width-1):
        pixel = image.getpixel((x,y))
        nearby_pixels=surrounding_pixels(x, y, image, 1, False)   
        if 255 in nearby_pixels and 0 in nearby_pixels:    # checks if the surrounding pixels have zero and are on the edge
            Boundary_array.append([x,y])

image2=image.copy()
width, height = image2.size

for values in range(len(Boundary_array)):
    x = Boundary_array[values][0]
    y = Boundary_array[values][1]
    # print(x,y)
    if 0 <= x < width and 0 <=y < height:
        image2.putpixel([x,y],255)
# print(width, height)
        
plt.imshow(image2)
plt.show() #image 2
im3 = ImageChops.subtract(image1 = image2, image2 = image)
plt.imshow(im3)
print("NOW")
plt.show()

new_image=im3


# plt.imshow(image2)
# print("now1")
# plt.show() #image 2
# plt.imshow(image)
# print("now2")
# plt.show() #image 2
# im3 = ImageChops.subtract(image1 = image2, image2 = image)
# print("now3")
# plt.imshow(im3)
# plt.show()

# new_image=im3
# npimage = np.array(new_image)


# width, height = npimage.shape

width, height = new_image.size
fig, ax = plt.subplots()
for x in range(width):
    for y in range(height):
        pixel_value=new_image.getpixel((x,y))
        if pixel_value > 100:
            new_image.putpixel((x,y),255)
        else:
            new_image.putpixel((x,y),0)

sip=0
for x in range(width):
    if sip == 1:
        break 
    for y in range(height):
        pixel_value=new_image.getpixel((x,y))
        if pixel_value > 0:
            next_pixel=(x,y)#
            print(next_pixel)
            start_pixel=next_pixel
            last_pixel=next_pixel
            sip=1
            break
       
reach=1
search=0
y_downlim=0
y_uplim=0
x_leftlim=0
x_rightlim=0
exup_array=[1,5,9]
exdown_array=[2,6,10]
exright_array=[3,7,11]
exleft_array=[4,8,12]
extension=1
leaf_outline = []
end = False
while len(leaf_outline) != len(Boundary_array):
    x , y = next_pixel
    
    # print(new_image.getpixel((x,y)))
    nearby_pixels_loc=surrounding_pixels(x, y, new_image, reach, True) 
    nearby_pixels=surrounding_pixels(x, y, new_image, reach, False)
    # print(next_pixel, " NEXT")
    # print(nearby_pixels)
    # print(nearby_pixels_loc)
    # print(leaf_outline)
    np=False
    pstop=0
    for pixels in range(len(nearby_pixels)):
        # print(pixels)
        pixs=nearby_pixels[pixels] 
        if pixs > 0: # add en else statement with reach ++
            if nearby_pixels_loc[pixels] not in leaf_outline:
                next_pixel=nearby_pixels_loc[pixels]
                x, y = next_pixel
                leaf_outline.append(next_pixel)
                new_image.putpixel([x,y],100)
                search=0
                y_downlim=0
                y_uplim=0
                x_leftlim=0
                x_rightlim=0
                extension=1
                reach=1
                last_pixel = next_pixel
                np=True
                break

    if np == False:
        if len(leaf_outline) > 20 and nearby_pixels_loc[pixels] == start_pixel:
            end=True
            print("Length > 20")
        else:
            # plt.imshow(new_image)
            # plt.pause(0.0000000000000000000000000000000000000000000000000000000000000000000000000001)
            # x,y=next_pixel
            reach+=1
            if reach > 4:
                reach=1
                if extension in exup_array:
                    x,y=last_pixel
                    y_uplim+=1
                    next_pixel=x,y-y_uplim
                    extension+=1
                    reach=1
                    print(extension, " UP")
                    print("Search: ", search)
                elif extension in exdown_array:
                    x,y=last_pixel
                    y_downlim+=1
                    next_pixel=x, y+y_downlim
                    extension+=1  
                    reach=1
                elif extension in exright_array:
                    x,y=last_pixel
                    x_rightlim+=1
                    next_pixel=x+x_rightlim,y
                    extension+=1    
                    reach=1
                elif extension in exleft_array:
                    x,y=last_pixel
                    x_leftlim+=1
                    next_pixel=x-x_leftlim,y
                    extension+=1
                    reach=1
                elif extension == 13 and search <= 10:
                    # plt.close()
                    search+=1
                    print(search, "SEARCH")
                    extension=1
                    reach=1
                    if len(leaf_outline) > 10 and search<11:
                        # print(len(leaf_outline))
                        next_pixel=leaf_outline[-search]
                        print(next_pixel)
                        x,y = next_pixel
                        last_pixel=next_pixel
                        # new_image.putpixel([x,y],50)
                elif search > 10:
                    print("END")
                    plt.close()
                    end=True
                    break

            
    if end==True:
        plt.close()
        break 


    # if not len(leaf_outline) % 100:
        # plt.close()
    if not len(leaf_outline) % 5:
        x1=x-20
        x2=x+20
        y1=y+20
        y2=y-20
        

        ax.imshow(new_image,origin="upper")

        # x1, x2, y1, y2 = 50, 50, 50, 50
        axins = ax.inset_axes([0.7, 0.7, 0.3, 0.3], xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
        # print(len(leaf_outline))
        axins.imshow(new_image, origin="lower")
        ax.indicate_inset_zoom(axins, edgecolor="black")
        plt.pause(0.01)
        plt.cla()
        # plt.close()

plt.show()
plt.close()
print(len(leaf_outline))

plt.imshow(new_image)
plt.show()#img 3
print(leaf_outline)

# x=324
# y=27

# x1=x-20
# x2=x+20
# y1=y+20
# y2=y-20


# fig, ax = plt.subplots()

# ax.imshow(image,origin="upper")

# # x1, x2, y1, y2 = 50, 50, 50, 50
# axins = ax.inset_axes(
#     [0.7, 0.7, 0.3, 0.3],
#     xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
# axins.imshow(image, origin="lower")
# ax.indicate_inset_zoom(axins, edgecolor="black")
# plt.show()



