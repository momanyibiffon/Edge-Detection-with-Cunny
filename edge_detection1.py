import cv2 as cv

img = cv.imread("horse.png")

# image scaled to get new dimensions
scale_percent = 20  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv.resize(img, dim, interpolation=cv.INTER_AREA)

# detect edges with Canny
edges = cv.Canny(image, 100, 100)

#dispay image edges
cv.imshow("Edges detected", edges)
cv.imshow("Original Image", image)

cv.waitKey(0)
cv.destroyAllWindows()
