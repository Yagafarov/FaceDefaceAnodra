import cv2
import numpy as np
from PIL import Image

def deface_image(img_path):
    # Haarcascade detektorlarni yuklaymiz
    face_cascade_default = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_cascade_alt = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    # Rasmni o‘qib olamiz va chegaralar bo‘yicha yuzlarni aniqlaymiz
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces_default = face_cascade_default.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    faces_alt = face_cascade_alt.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    faces = np.concatenate((faces_default, faces_alt), axis=0)

    # Aniqlangan yuzlarga filtrlar qo‘yamiz va rasmga qayta qo‘llaymiz
    for (x, y, w, h) in faces:
        roi = image[y:y + h, x:x + w]
        roi = cv2.GaussianBlur(roi, (55, 55), 100)
        image[y:y + h, x:x + w] = roi

    # Rasmni saqlaymiz
    output_path = "test/defaced_" + img_path.split('/')[-1]
    cv2.imwrite(output_path, image)
    return output_path

def clear_exif(img_path):
    image = Image.open(img_path)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    output_path = "test/exif_cleared_" + img_path.split('/')[-1]
    image_without_exif.save(output_path)
    return output_path


if __name__ == "__main__":
    print("Bu modul xususiyatlari uchun boshlang'ich ishlab chiqilgan.")
