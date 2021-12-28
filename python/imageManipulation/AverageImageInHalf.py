import numpy as np
import cv2
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('-l', '--load-image', help='Put the image in the same folder as the script and send in the argument to load it', dest='load_images')

    options = parser.parse_args()
    image = cv2.imread(options.load_images, cv2.IMREAD_COLOR)
    newImage = np.zeros((int(image.shape[0] / 2), int(image.shape[1] / 2), image.shape[2]), np.uint8)

    for x in range(newImage.shape[0]):
        for y in range(newImage.shape[1]):
            for color in range(newImage.shape[2]):
                newImage[x][y][color] = int((int(image[x*2][y*2][color])+
                            int(image[x*2+1][y*2][color])+
                            int(image[x*2][y*2+1][color])+
                            int(image[x*2+1][y*2+1][color]))/4)

    cv2.imwrite('cutInHalf'+options.load_images, newImage);


if __name__ == "__main__":
    main()
