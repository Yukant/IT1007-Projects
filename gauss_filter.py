from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np
import imageio


def blur_image(filename):
    pic = imageio.imread_v2(filename)
    blurred_pic = ndimage.gaussian_filter(pic, sigma=(5,5,1))

    plt.imshow(blurred_pic)
    # plt.imsave("blur_image_output.jpg",blurred_pic)
    plt.show()

# blur_image("cute cat.jpg")
