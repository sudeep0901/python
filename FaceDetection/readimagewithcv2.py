import numpy as np
import cv2

img = cv2.imread('image.jpg')
# print(img)

while True:

    cv2.imshow('mandrill', img)

    if cv2.waitKey(1) & 0xFF == 27: # getting escape key
        break
        
cv2.imwrite("final_image.png", img)

cv2.destroyAllWindows()


