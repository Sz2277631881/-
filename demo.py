from sympy import resultant
from ultralytics import YOLO
yolo = YOLO("./yoloV8n.pt", task="detect")
result=yolo(source="yoloV8-main-ultralytics/ultralytics/assets/zidane.jpg")
