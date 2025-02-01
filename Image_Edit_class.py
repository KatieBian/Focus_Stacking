import cv2
import numpy as np
import os

class Image_Editor():
    def __init__(self):
        pass

    def find_smallest_dimensions(self, file_path):
        '''Iterate through each image file to find smallest pixel height and width. Used to resize image.'''

        list_of_dim_ratios = []
        smallest_height = np.inf
        smallest_width = np.inf

        directory = os.fsencode(file_path)
    
        for img in os.listdir(directory):
            img_name = os.fsdecode(img)
            if img_name.endswith(".png"):
                image = cv2.imread(file_path + "\\" + img_name)
                
                if image.shape[0] < smallest_height:
                    smallest_height = image.shape[0]
                if image.shape[1] < smallest_width:
                    smallest_width = image.shape[1]
                
                #list_of_dim_ratios.append(image.shape[0]/image.shape[1])
        
        return smallest_height, smallest_width


    def resize(self, file_path):
        '''Resize images to be same dimensions.'''

        new_height, new_width = self.find_smallest_dimensions(file_path)

        directory = os.fsencode(file_path)
    
        for img in os.listdir(directory):
            img_name = os.fsdecode(img)
            if img_name.endswith(".png"):
            
                image = cv2.imread(file_path + "\\" + img_name)
                new_image = cv2.resize(image,(new_width,new_height))
                new_img_name = file_path + "\\resized_" + img_name
                cv2.imwrite(new_img_name, new_image)
                cv2.imshow("resized image",new_image)



if __name__ == "__main__":
    image = Image_Editor()
    image.resize(r"D:\PHY427\OPMI\focus stacking\trial 1_FPS34.8_Frames20_delay0.5s")
