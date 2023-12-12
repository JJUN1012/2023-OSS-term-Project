import cv2

# Load the image
image = cv2.imread('image/cars1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained Haar Cascade car classifier
car_cascade = cv2.CascadeClassifier('cars4.xml')

# Detect cars
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

print(f'Number of cars detected: {len(cars)}')

# Draw rectangle around the cars
for (x, y, w, h) in cars:
    padding = 20  # Adjust this value to your preference
    cv2.rectangle(image, (x+padding, y+padding), (x+w-padding, y+h-padding), (0, 0, 255), 2)


# Display the output
cv2.imshow('Car Detection', image)
cv2.waitKey()
