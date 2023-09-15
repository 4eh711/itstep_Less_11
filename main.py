import cv2
from PIL import Image

image_path = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('glasses.png')
smile = Image.open('smile.png')
cap = Image.open('cap_1.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
smile = smile.convert("RGBA")
cap = cap.convert("RGBA")

print(cat_face)
#for (x,y,w,h) in cat_face:
    #glasses = glasses.resize((w, int(h/3)))
    #cat = cat.paste(glasses, (x, int(y+h/4)), glasses)

#cat.save("cat_with_glasses.png")
#cat_with_glasses = cv2.imread("cat_with_glasses.png")
#cv2.imshow("Cat_with_glasses", cat_with_glasses)
#cv2.waitKey()

for (x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    smile = smile.resize((int(w / 2), int(h / 4)))
    cat.paste(smile, (x+20, int(y/3 + h)), smile)
    cap = cap.resize((w+50, h+20))
    cat.paste(cap, (x-30, y-55), cap)


cat.save("cat_with_glasses.png")
cat_with_glasses = cv2.imread("cat_with_glasses.png")
cv2.imshow("Cat_with_glasses", cat_with_glasses)
cv2.waitKey()  # Ждем, пока пользователь закроет окно
#cv2.destroyAllWindows()


    #cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255),3)


#cv2.imshow("Cat", image)
#cv2.waitKey()

