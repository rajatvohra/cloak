import numpy as np 
import time
import cv2


def get_hsv(colour):
    if(colour.lower()=='red'):
        lower_col = np.array([0, 120, 50])
        upper_col = np.array([10, 255,255])
        lower_col1 = np.array([170, 120, 70])
        upper_col1 = np.array([180, 255, 255])
    elif(colour.lower() == 'blue'):
        lower_col = np.array([100, 100, 50])
        upper_col = np.array([110, 255,255])
        lower_col1 = np.array([110, 100, 50])
        upper_col1 = np.array([130, 255, 255])
    elif(colour.lower()=='green'):
        lower_col = np.array([45, 100, 50])
        upper_col = np.array([60, 255,255])
        lower_col1 = np.array([60, 100, 70])
        upper_col1 = np.array([75, 255, 255])
    elif(colour.lower()=='yellow'):
        lower_col = np.array([25, 60, 50])
        upper_col = np.array([30, 255,255])
        lower_col1 = np.array([30, 60, 50])
        upper_col1 = np.array([35, 255, 255])
    else:
        print("this colour is not in our pallete ,sorry")
        exit()

    return lower_col,upper_col,lower_col1,upper_col1
def invisible(lower_col,upper_col,lower_col1,upper_col1):
    inp= cv2.VideoCapture(0)
    time.sleep(3)
    count = 0
    background = 0
    for i in range(60): 
        return_val, background = inp.read() 
        if return_val == False : 
            continue 
    flipped_background = np.flip(background, axis = 1)
    while (inp.isOpened()): 
        return_val, img = inp.read() 
        img=np.flip(img,axis=1)
        if not return_val : 
            break 
        flipped_img=np.flip(img,axis=1)
        #####mask for green colour#####
        hsv = cv2.cvtColor(flipped_img, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, lower_col, upper_col)
        mask2 = cv2.inRange(hsv, lower_col1, upper_col1)

        mask = mask1 + mask2
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
        mask1=cv2.bitwise_not(mask)

        final1=cv2.bitwise_and(flipped_img,flipped_img,mask=mask1)
        final2=cv2.bitwise_and(flipped_background,flipped_background,mask=mask)
        output=cv2.add(final1,final2)
        cv2.imshow("watch magic happen",output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            inp.release()
            cv2.destroyAllWindows()
            break

####main#####
colour=input("which colour do you want to make invisible \n")
lower_col,upper_col,lower_col1,upper_col1=get_hsv(colour)
invisible(lower_col,upper_col,lower_col1,upper_col1)




