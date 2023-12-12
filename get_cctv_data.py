import cv2
import numpy as np
import requests
from io import BytesIO

# API URL 및 이미지 요청
api_url = "YOUR_API_URL"  # 실제 API URL로 변경
response = requests.get(api_url)
img_bytes = BytesIO(response.content)
img = cv2.imdecode(np.asarray(bytearray(img_bytes.read()), dtype=np.uint8), cv2.IMREAD_COLOR)

# 그레이 스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 차량 검출을 위한 이미지 전처리
# (이미지의 크기, 스레시홀드 등을 조절하여 최적의 결과를 얻을 수 있습니다.)
# 여기서는 간단한 가우시안 블러 및 케니 에지 검출을 사용합니다.
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 140, 220)

# 차량 개수를 세기 위한 컨투어 검출
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 차량 개수 출력
vehicle_count = len(contours)
print(f"차량 개수: {vehicle_count}")

# 결과 이미지에 차량 윤곽선 그리기
result_img = img.copy()
cv2.drawContours(result_img, contours, -1, (0, 255, 0), 2)

# 차량 개수에 따라 메시지 출력
if vehicle_count >= 50:
    message = "정체입니다. 졸음 운전에 주의하세요"
else:
    message = "도로 상황이 쾌적합니다. 서행하세요"

# 메시지 출력
cv2.putText(result_img, message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# 결과 이미지 출력
cv2.imshow("Vehicle Count", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#will be get from user
