from ultralytics import YOLO

model = YOLO('runs/detect/stop_sign_model-12/weights/best.pt')

results = model.predict(source='../stop_sign_dataset', conf = 0.2, save = True)