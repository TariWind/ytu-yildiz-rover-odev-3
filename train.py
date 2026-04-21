from roboflow import Roboflow
from ultralytics import YOLO



rf = Roboflow(api_key = "z3HMjF0iRaCQn0nYPYnq" )
project = rf.workspace("stardust").project("stop-sign-ocamr")
version = project.version(1)
dataset = version.download("yolov8")

def train_model():

    model = YOLO('yolov8n.pt')

    model.train(
    data = 'STOP-SIGN-1/data.yaml',
    epochs = 50,
    imgsz = 640,
    batch = 4,
    name = 'stop_sign_model',
    device = 0
    )

if __name__ == '__main__':
    train_model()



