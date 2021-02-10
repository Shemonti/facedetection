import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('20180807_181851.jpg',1)

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray_img,1.1,4)

print(type(faces))
print(faces)

# for x,y,w,h in faces:
#     img=cv2.rectangle(img, (x+y), (x+w,y+h), (255, 0, 0),1)

for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),6)
resized=cv2.resize(img,(200,200) )
cv2.imshow("dia",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()