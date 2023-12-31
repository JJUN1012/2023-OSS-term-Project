import cv2
import numpy as np
import urllib.request

def get_how_many_cars(url):
    # YOLO model road
    net = cv2.dnn.readNet("datafiles/yolov3.weights", "datafiles/yolov3.cfg")
    layer_names = net.getUnconnectedOutLayersNames()

    # List of class
    classes = []
    with open("datafiles/coco.names", "r") as f:
        classes = [line.strip() for line in f]
    # Input url

    urllib.request.urlretrieve(url, "datafiles/local_image.jpg")

    # Image road
    image = cv2.imread("datafiles/local_image.jpg")
    height, width, _ = image.shape

    # Description of pre-image processing and model input
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Perform yolo object detection
    outs = net.forward(layer_names)

    # Extracting information from detected objects
    conf_threshold = 0.45
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold and classes[class_id] == "car":
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # Remove Overlapping Boxes (Non-maximum suppression)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, 0.4)

    # Number of cars output
    print("Number of cars:", len(indices))
    # Output of the resulting image
    # for i in indices:
    #     box = boxes[i]
    #     x, y, w, h = box
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     cv2.putText(image, f'Car {i + 1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # cv2.imshow("IMAGE",image)
    # cv2.waitKey(0)
    return len(indices)

#Test
if __name__ == "__main__":
    get_how_many_cars("http://cctvsec.ktict.co.kr:8090/18/IOd8QeDX9z1ZfoUzd3iohahB19J8Z0PntWecI6NHe9bN/8wawDiqUxFukQVuMCitwtu4DZ7s+hv+pt4i/KVNnQ==")