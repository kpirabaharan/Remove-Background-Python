import sys
import cv2
import numpy as np


def main():
    # Display Full Untruncated Image
    np.set_printoptions(threshold=sys.maxsize)

    # Save image in set directory
    # Read RGB image
    img = cv2.imread("Shirts_Board.png")

    # Convert RGB to Grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    grayscale_blur = cv2.GaussianBlur(grayscale, (5, 5), 1, sigmaY=1)

    # Apply Threshold
    _, alpha = cv2.threshold(grayscale_blur, 215, 255, cv2.THRESH_BINARY_INV)

    # Split Colors from Original Image
    b, g, r = cv2.split(img)

    # List of Channels
    rgba = [b, g, r, alpha]

    # print(rgba)

    dst = cv2.merge(rgba, 4)

    cv2.imwrite("Destination.png", dst)

    # Output img with window name as 'image'
    # cv2.imshow("image", img)
    # cv2.imshow("grayscale", grayscale)

    # Print Image Shape and Map
    # print(img.shape)
    # print(img)

    # Maintain output window until
    # user presses a key
    # cv2.waitKey(0)

    # Destroying present windows on screen
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
