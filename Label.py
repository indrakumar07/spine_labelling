import cv2
import imutils

img1= cv2.imread("I490(orig).png")
img2= cv2.imread('I490-label.png')
h1,w1= img1.shape[:2]
h2,w2= img2.shape[:2]


if ((h1==h2)and(w1==w2)):
    for i in range(h1):
        for j in range(w1):
            if (img2[i,j]!= (0,0,0)).all():
                img1[i,j]= (255,255,255)
            j=j+1
        i=i+1
else:
    print("height and width of two images are not equal")
    
  
def plotting(lst,st):
    x=0
    no=range(1,13)
    for c in lst:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.drawContours(img1, [c], -1, (0,  255, 0), 2)
        cv2.circle(img1, (cX, cY), 2, (255, 0, 0), -1)    
        cv2.putText(img1, st+str(no[x]), (cX - 0, cY - 0),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.imshow("Image", img1)
        cv2.waitKey(0)
        x=x+1
    
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (1, 1), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(blurred, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
i=0
for x in cnts:
    M = cv2.moments(x)
    if(M["m00"]==0):
        cnts.pop(i)
    i=i+1
        
plotting(cnts[-1:-8:-1],"--C")
plotting(cnts[-8:-20:-1],"--T")
plotting(cnts[-20:-25:-1],"--L")

print(len(cnts))


# Cervical - C1 to C7
# Thoracic - T1 to T12
# Lumbar - L1 to L5