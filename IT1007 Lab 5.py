from scipy import misc, ndimage
import imageio
import matplotlib.pyplot as plt
import numpy as np
from circle_pic import circle_pic
import circle_pic
import gauss_filter
import rotate_image


# Complete Q1 below
def show_an_image(filename):
    filename = imageio.imread_v2(filename)
    plt.imshow(filename)
    plt.show()


# Complete Q2 below
def put_behind_bar(filename):
    read_filename = imageio.imread_v2(filename)
    for i in range(0, read_filename.shape[0]):
        for j in range(0, read_filename.shape[1]):
            if (j // 50) % 2 == 0:
                read_filename[i][j] = 0
    # misc.imsave('put_behind_bar.jpg', read_filename)
    plt.imshow(read_filename)
    plt.show()

    return


# Complete Q3 below
def mirror_image(filename):
    filename1 = imageio.imread_v2(filename)
    new_image = imageio.imread_v2(filename)
    newimage = imageio.imread_v2(filename)
    for i in range(filename1.shape[0]):
        for j in range(filename1.shape[1]):
            w = filename1.shape[1]
            n = (w - j - 1)
            new_image[i][j] = filename1[i][n]
            newimage[i][j] = (new_image[i][j] / 2 + filename1[i][j] / 2)

    # misc.imsave('mirror_image_output.jpg', filename1)
    plt.imshow(newimage)
    plt.show()


# Complete Q4 below
def put_behind_bar_transparent(filename):
    filename = imageio.imread_v2(filename)
    for i in range(0, filename.shape[0]):
        for j in range(0, filename.shape[1]):
            if (j // 50) % 2 == 0:
                filename[i][j] = filename[i][j] / 2
    # misc.imsave('put_behind_bar_transparent_output.jpg', filename)
    plt.imshow(filename)
    plt.show()


# Complete Q5 below
def image_processor():
    function_dict = {'1': show_an_image, '2': mirror_image, '3': put_behind_bar, '4': put_behind_bar_transparent,
                     '5': circle_pic.circle_pic, '6': gauss_filter.blur_image, '7': rotate_image.rotate_image,
                     'Q': quit}
    print("Welcome to IT1007 Image Processsor!")
    filename = input('Please enter the file name: ')
    print('Please select an operation you want to perform ')
    print(
        '1. Show an image\n' + '2. Mirror image\n' + '3. Put behind bar\n' + '4. Put behind transparent bar\n' + '5. Circle picture\n' + '6. Blurring\n' + '7. Rotation\n' + 'Q. Quit\n')
    while (1):
        action = input('Enter your choice(1-7,Q): ')
        if action in function_dict:
            function_dict[action](filename)
        else:
            print('Invalid choice!')


# uncomment the following for your own testing
# show_an_image('cute cat.jpg')
# put_behind_bar("cute cat.jpg")
# mirror_image('cute cat.jpg')
put_behind_bar_transparent('cute cat.jpg')
# image_processor()

