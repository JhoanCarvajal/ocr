import cv2
import pytesseract
import llenar_excel

def ocr(ruta):
    imagen = cv2.imread(ruta, 0)
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    ROI = image[993:993+381,1429:1429+741]
    ROI2 = image[153:153+133,3065:3065+869]

    print("texto de roi1")
    data = pytesseract.image_to_string(ROI)
    print(data)
    print("--------------------------------")
    lista_consumo = data.split()

    print("texto de roi2")
    data2 = pytesseract.image_to_string(ROI2)
    print(data2)
    print("--------------------------------")
    lista_total = data2.split()

    #cv2.imshow('imagen redimencionada', image)
    #cv2.imshow('ROI', ROI)
    #cv2.imshow('ROI2', ROI2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    llenar_excel.llenar(lista_consumo, lista_total)