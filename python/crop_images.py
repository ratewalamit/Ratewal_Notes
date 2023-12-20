from PIL import Image
import glob
import os
import sys

def crop_image(image_path,from_top=100,from_bottom=1020,from_left=20,from_right=25):  #from_left tell how much area to crop from left
    # Opens a image in RGB mode
    im = Image.open(image_path)   #image path need to be full path
    width, height = im.size
    # Setting the points for cropped image
    left = 0+from_left
    top = 0+from_top
    right = width-from_right
    bottom = height-from_bottom
    
    cropped_img = im.crop((left, top, right, bottom))
    
    #im.show()
    #cropped_img.show()
    return cropped_img


def vertically_concat_images(img1,img2):
    images_list = [img1, img2]
    imgs = [Image.open(i) for i in images_list]
    min_img_width = min(i.width for i in imgs)
    total_height = 0
    for i, img in enumerate(imgs):
        if img.width > min_img_width:
            imgs[i] = img.resize((min_img_width, int(img.height / img.width * min_img_width)), Image.ANTIALIAS)
        total_height += imgs[i].height

    img_merge = Image.new(imgs[0].mode, (min_img_width, total_height))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0, y))
        y += img.height
        #img_merge.save('terracegarden_v.jpg')
    return img_merge



def vertically_concat_images_from_rgb_format(img1,img2):
    #these are rgb images, Not stored jpg images
    imgs = [img1,img2]
    min_img_width = min(i.width for i in imgs)
    total_height = 0
    for i, img in enumerate(imgs):
        if img.width > min_img_width:
            imgs[i] = img.resize((min_img_width, int(img.height / img.width * min_img_width)), Image.ANTIALIAS)
        total_height += imgs[i].height

    img_merge = Image.new(imgs[0].mode, (min_img_width, total_height))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0, y))
        y += img.height
        #img_merge.save('terracegarden_v.jpg')
    return img_merge


if __name__=="__main__":

    image_folder="/home/amitk/Copy"
    dirs = os.listdir(image_folder)
    image_list=glob.glob(f"{image_folder}/Screenshot_*.png")
    cropped_header=crop_image("/home/amitk/Copy/header.png",from_top=0,from_bottom=0,from_left=20,from_right=25)
    for item in image_list:
        if os.path.isfile(item):
            print(f"Done for: {item}")
            cropped_Image=crop_image(item)
            final_cropped_header_merged_image=vertically_concat_images_from_rgb_format(cropped_header,cropped_Image)
            final_cropped_header_merged_image.save(image_folder + f'/Cropped_{os.path.basename(item)}', "png", quality=100)


