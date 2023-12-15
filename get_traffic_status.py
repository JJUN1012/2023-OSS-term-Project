import get_how_many_cars_with_YOLO as gcy

def get_traffic_status(url):
    car_count = gcy.get_how_many_cars(url)

    if car_count <= 10:
        print("Good: Traffic flow is smooth.")
    elif 10 < car_count <= 20:
        print("Slow down: Traffic is a bit congested.")
    else:
        print("Congestion: Traffic congestion is expected.")
