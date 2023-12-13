import cv2
import numpy as np
import urllib.request

def get_how_many_cars(url):
    # YOLO 모델 로드
    net = cv2.dnn.readNet("datafiles/yolov3.weights", "datafiles/yolov3.cfg")
    layer_names = net.getUnconnectedOutLayersNames()

    # 클래스의 목록
    classes = []
    with open("datafiles/coco.names", "r") as f:
        classes = [line.strip() for line in f]
    #input url

    urllib.request.urlretrieve(url, "datafiles/local_image.jpg")

    # 이미지 로드
    image = cv2.imread("datafiles/local_image.jpg")
    height, width, _ = image.shape

    # 이미지 전처리 및 모델 입력 설정
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # YOLO 객체 감지 수행
    outs = net.forward(layer_names)

    # 감지된 객체의 정보 추출
    conf_threshold = 0.5
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

    # 겹치는 박스 제거 (Non-maximum suppression)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, 0.4)

    # 자동차 개수 출력
    print("자동차 개수:", len(indices))
    # 결과 시각화
    for i in indices:
        box = boxes[i]
        x, y, w, h = box
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'Car {i + 1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 결과 이미지 출력
    cv2.imshow("IMAGE",image)
    cv2.waitKey(0)

if __name__ == "__main__":
    get_how_many_cars("http://cctvsec.ktict.co.kr:8090/540/xFbPY5jkSvcDdSiuLa2v+SqYOmH39pxfPjptCnjKwClta2qvinkL5zKUt9tjbzrG+JIDOpQZHroIHG/ptnoJ2g==")