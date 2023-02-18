# определение номера машины из камеры видеонаблюдения и вывод номера
# для дальнейшего использования номера машины в опознавательной системе

import matplotlib.pyplot as plt
import pytesseract
import cv2
from PIL import Image


def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(carplate_img)
    plt.show()

    return carplate_img


def carplate_extract(image, carplate_haar_cascade):
    carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=3)
    counter = 0
    for x, y, w, h in carplate_rects:
        carplate_img = image[y + 15:y + h - 10, x + 15:x + w - 20]
        counter += 1
    print(counter)
    return carplate_img


def enlarge_img(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    plt.axis('off')
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return resized_image


def main():
    carplate_img_rgb = open_img(img_path='C:\pythonProject2023\cars\im_4.jpg')
    carplate_haar_cascade = cv2.CascadeClassifier('C:\pythonProject2023\znaki.xml')

    carplate_extract_img = carplate_extract(carplate_img_rgb, carplate_haar_cascade)
    carplate_extract_img = enlarge_img(carplate_extract_img, 150)
    plt.imshow(carplate_extract_img)
    plt.show()

    carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
    plt.axis('off')
    plt.imshow(carplate_extract_img_gray, cmap='gray')
    # plt.show()

    pytesseract.pytesseract.tesseract_cmd = r'C:\pythonProject2023\venv\Lib\site-packages\tesseract.exe'
    # print(pytesseract.image_to_string(Image.open('C:\pythonProject2023\cars\im_3.jpg')))
    target1 = pytesseract.image_to_string(carplate_extract_img_gray, lang='eng',
                                          config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    # target2 = pytesseract.image_to_string(carplate_extract_img_gray, lang='eng',
    #                                      config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    result = ''
    for i in target1:
        if i != '1':
            result += i
    print(result)


print('0', 'O')

if __name__ == '__main__':
    main()
