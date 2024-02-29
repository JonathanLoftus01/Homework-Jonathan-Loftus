import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from PIL import Image
from PIL import Image, ImageChops
import os 
import csv

image_path = "C:\\Users\\jonat\\Documents\\CODE lancashire\\Python CODE LANCS\\python homework\\leaf siloetes\\data\\data"
outline_path = "C:\\Users\\jonat\\Documents\\CODE lancashire\\Python CODE LANCS\\python homework\\leaf siloetes\\data\\outlines"

# columns_titles=["Genus", "species", "Individual", "leaf 1/4", "leaf 2/4", "leaf 3/4", "leaf 4/4" "leaf size"]
columns_titles=["Genus", "species", "Individual", "Leaf_route_1" , "Leaf_route_2", "Leaf_route_3", "Leaf size", "Leaf height", "Leaf width"]
csv_file_path = "leaf outlines.csv"
with open(csv_file_path, mode="w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(columns_titles)

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

Genus_array=[]
species_array=[]
Individual_array=[]
leaf_outline_array=[]

redo_c1=0

genus_species= os.listdir(image_path) # collection of species names stings
for species in genus_species:
    # print(genus_species)
    image_path2=image_path + "\\" + species
    IndImage = os.listdir(image_path2)
    print(IndImage)
    for individuals in IndImage:
        # print(image_path2 + "\\" + IndImage[p])
        image = Image.open(image_path2 + "\\" + individuals)
        print(individuals)

        # plt.imshow(image)
        # plt.show()
        Individual_array.append(individuals)
        
        if species.count("_")==2:
            Genus, middle, species_ = species.split("_")
            Genus_array.append(Genus + species_)
            species_array.append(middle)
        elif species.count("_")==1:
            Genus, species_ = species.split("_")
            Genus_array.append(Genus)
            species_array.append(species_)
        else:            
            species_= 0
            Genus_array.append(species)
            species_array.append(species_)

        width, height = image.size

        Boundary_array=[]

        for y in range(height-1):
            for x in range(width-1):
                pixel = image.getpixel((x,y))
                nearby_pixels=surrounding_pixels(x, y, image, 1, False)   
                if 255 in nearby_pixels and 0 in nearby_pixels:    # checks if the surrounding pixels have zero and are on the edge
                    Boundary_array.append([x,y])

        image2 = image.copy()
        width, height = image2.size


        for x in range(width):
            for y in range(height):
                image2.putpixel([x,y],0)

        for values in Boundary_array:
            x,y = values
            if 0 <=y < height and 0 <= x < width:
                image2.putpixel([x,y], 255)


        plt.imshow(image2)
        # plt.show() #image 2
        im3 = ImageChops.subtract(image1 = image2, image2 = image)
        plt.imshow(im3)
        # plt.show()

        new_image=im3
        width, height = new_image.size

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
                    # print(next_pixel)
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
                    # print("Length > 20")
                else:
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
                            # print(extension, " UP")
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
                        elif extension == 13 and search <=10:
                            search+=1
                            # print(search)
                            extension=1
                            reach=1
                            if len(leaf_outline) > 11 and search < 11:
                                # print(len(leaf_outline))
                                next_pixel=leaf_outline[-search]
                                x,y=next_pixel
                                last_pixel=next_pixel
                        elif search > 10:
                            print("END")
                            end=True
                            break
            
            if end==True:
                break 

        test_image=new_image.copy()
        if os.path.exists(outline_path + "\\" + species):
            test_image=test_image.save(outline_path + "\\" + species + "\\" + individuals)
        else:
            os.makedirs(outline_path + "\\" + species)
            test_image=test_image.save(outline_path + "\\" + species + "\\" + individuals)
        # leaf_outline_array.append(leaf_outline)
        x_outline=[]
        y_outline=[]
        leaf_half_1=leaf_outline[0:int(len(leaf_outline)*0.33)]
        leaf_half_2=leaf_outline[int(len(leaf_outline)*0.33):int(len(leaf_outline)*0.66)]
        leaf_half_3=leaf_outline[int(len(leaf_outline)*0.66):]
        lock=0
        for coors in range(len(leaf_half_1)):
            if lock == 0:
                STR_x = str(leaf_half_1[coors][0]) + "," + str(leaf_half_1[coors][1])
                # STR_y = str(leaf_outline[coors][1])
                lock = 1
            else:
                STR_x = STR_x + "|" + str(leaf_half_1[coors][0]) + "," + str(leaf_half_1[coors][1])

        lock=0
        for coors in range(len(leaf_half_2)):
            if lock == 0:
                STR_y = str(leaf_half_2[coors][0]) + "," + str(leaf_half_2[coors][1])
                # STR_y = str(leaf_outline[coors][1])
                lock = 1
            else:
                STR_y = STR_y + "|" + str(leaf_half_2[coors][0]) + "," + str(leaf_half_2[coors][1])
        
        lock=0
        for coors in range(len(leaf_half_3)):
            if lock == 0:
                STR_z = str(leaf_half_3[coors][0]) + "," + str(leaf_half_3[coors][1])
                # STR_y = str(leaf_outline[coors][1])
                lock = 1
            else:
                STR_z = STR_z + "|" + str(leaf_half_3[coors][0]) + "," + str(leaf_half_3[coors][1])
                # STR_y = STR_y + "|" + str(leaf_outline[coors][1])
        # print(type(x_outline))
        # Leaf_1= leaf_outline[0:int(len(leaf_outline)/4)]
        # Leaf_2= leaf_outline[int(len(leaf_outline)/4):int(len(leaf_outline)/2)]
        # Leaf_3= leaf_outline[int(len(leaf_outline)/2):int(len(leaf_outline)*0.75)]
        # Leaf_4= leaf_outline[int(len(leaf_outline)*0.75):]

        # lock=0
        # for coors in range(len(Leaf_1)):
        #     if lock == 0:
        #         Leaf_1_4=str(Leaf_1[coors][0]) + "," + str(Leaf_1[coors][1])
        #         lock+=1
        #     else: 
        #         Leaf_1_4= Leaf_1_4 + "|" + str(Leaf_1[coors][0]) + "," + str(Leaf_1[coors][1])

        # lock=0
        # for coors in range(len(Leaf_2)):
        #     if lock == 0:
        #         Leaf_2_4=str(Leaf_2[coors][0]) + "," + str(Leaf_2[coors][1])
        #         lock+=1
        #     else: 
        #         Leaf_2_4= Leaf_2_4 + "|" + str(Leaf_2[coors][0]) + "," + str(Leaf_2[coors][1])

        # lock=0
        # for coors in range(len(Leaf_3)):
        #     if lock == 0:
        #         Leaf_3_4=str(Leaf_3[coors][0]) + "," + str(Leaf_3[coors][1])
        #         lock+=1
        #     else: 
        #         Leaf_3_4= Leaf_3_4 + "|" + str(Leaf_3[coors][0]) + "," + str(Leaf_3[coors][1])

        # lock=0
        # for coors in range(len(Leaf_4)):
        #     if lock == 0:
        #         Leaf_4_4=str(Leaf_4[coors][0]) + "," + str(Leaf_4[coors][1])
        #         lock+=1
        #     else: 
        #         Leaf_4_4= Leaf_4_4 + "|" + str(Leaf_4[coors][0]) + "," + str(Leaf_4[coors][1])
 
        size=len(leaf_outline)
        print(size)
        # data=[Genus, species_, individuals, Leaf_1_4, Leaf_2_4, Leaf_3_4, Leaf_4_4, size]
        data=[Genus, species_, individuals, STR_x, STR_y, STR_z, size, height, width]
        # print(data)
        


        with open(csv_file_path, mode="a", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(data)

        # if redo_c1==0:
        #     with open(csv_file_path, mode="a", newline='') as csvfile:
        #         csv_writer = csv.writer(csvfile)
        #         csv_writer.writerow(data)
        #     redo_c1=1
        Genus_array=[]
        species_array=[]
        Individual_array=[]
        leaf_outline_array=[]

        # plt.imshow(test_image)
        # plt.show()





        # genus_list = []

        # for values in genus_species:
            # genus = values.split("_")
            # genus_list.append(genus[0])
            

        # print(set(genus_list))