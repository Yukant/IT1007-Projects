import imageio
import matplotlib.pyplot as plt
import numpy as np

def circle_pic(filename):
    pic = imageio.imread_v2(filename)
    xlen, ylen = pic.shape[0], pic.shape[1]
    xcenter, ycenter = xlen/2, ylen/2

    pic2 = np.array(pic)
    for i in range(xlen):
        for j in range(ylen):
            if (i-xcenter)**2 + (j-ycenter)**2 > (xlen/3)**2:
                pic2[i][j] = pic2[i][j]/2

    plt.imshow(pic2)
    # plt.imsave("circle_pic_output.jpg",pic2)
    plt.show()

# circle_pic("cute cat.jpg")


