import cv2
import numpy as np

# 전역 변수 초기화
drawing = False  # 드로잉 상태
points = []  # 클릭한 점 저장


# 마우스 클릭 이벤트 핸들러
def draw_circle(event, x, y, flags, param):
    global drawing, points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points.append((x, y))  # 클릭한 좌표 추가

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x, y))

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points.append((x, y))


# 카메라에서 비디오 캡처
cap = cv2.VideoCapture(0)

cv2.namedWindow('Safety Zone')
cv2.setMouseCallback('Safety Zone', draw_circle)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 점 연결
    if len(points) > 1:
        cv2.polylines(frame, [np.array(points)], isClosed=True, color=(0, 255, 0), thickness=2)

    cv2.imshow('Safety Zone', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # 'q' 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()
