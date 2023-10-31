import sys

import cv2
import numpy as np


def main():
    # Display Full Untruncated Image
    np.set_printoptions(threshold=sys.maxsize)

    # Save image in set directory
    # Read RGB image
    img = cv2.imread("Shirts_Board.jpeg")

    # Output img with window name as 'image'
    cv2.imshow("image", img)

    # Print Image Shape and Map
    print(img.shape)
    print(img)

    # Maintain output window until
    # user presses a key
    cv2.waitKey(0)

    # Destroying present windows on screen
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
