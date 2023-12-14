import cv2

def open_video(url):
    cap = cv2.VideoCapture(url)
    print("Q를 눌러 영상을 종료할 수 있습니다.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video Stream', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    open_video("http://cctvsec.ktict.co.kr/540/xFbPY5jkSvcDdSiuLa2v+SqYOmH39pxfPjptCnjKwClta2qvinkL5zKUt9tjbzrGzXKvQQdf5XoDcaVusAZ+EA==")