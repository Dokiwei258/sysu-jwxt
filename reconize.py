import cv2
import linerid
from pytesseract import image_to_string
def Pic2String(path):
   im = linerid.getridofline(path)  # 处理图片去噪
#contours, hierarchy = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   text = image_to_string(im)
   text=text[0:4]
   return text