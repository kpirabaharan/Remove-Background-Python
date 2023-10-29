import cv2
from PIL import Image


def main():
    # Save image in set directory
    # Read RGB image
    img = cv2.imread("Shirts_Board.jpeg")

    # Output img with window name as 'image'
    cv2.imshow("image", img)

    # Maintain output window until
    # user presses a key
    cv2.waitKey(0)

    # Destroying present windows on screen
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
