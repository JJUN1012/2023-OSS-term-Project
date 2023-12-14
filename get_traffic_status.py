import get_how_many_cars_with_YOLO as gcy



def get_traffic_status(url):
    car_count = gcy.get_how_many_cars(url)

    if car_count <= 10:
        print("양호: 교통 흐름이 원활합니다.")
    elif 10 < car_count <= 20:
        print("서행: 교통이 다소 혼잡합니다.")
    else:
        print("정체: 교통 정체가 예상됩니다.")

if __name__ == "__main__":
    get_traffic_status("http://cctvsec.ktict.co.kr:8090/540/xFbPY5jkSvcDdSiuLa2v+SqYOmH39pxfPjptCnjKwClta2qvinkL5zKUt9tjbzrG+JIDOpQZHroIHG/ptnoJ2g==")
