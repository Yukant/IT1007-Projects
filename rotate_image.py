from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np
import imageio
def rotate_image(filename):
    pic = imageio.imread_v2(filename)
    rotate_1 = ndimage.rotate(pic, 45)
    rotate_1_noreshape = ndimage.rotate(pic, 45, reshape=False)

    plt.subplot(121)
    plt.imshow(rotate_1)
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(rotate_1_noreshape)
    plt.axis('off')
    # plt.imsave("rotate_image_noreshape_output.jpg",rotate_1_noreshape)
    plt.show()

# rotate_image("cute cat.jpg")