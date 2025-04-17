from PIL import Image

for i in range(1,27):
    img = Image.open(f"test_camera_image_{i}.jpg")
    img = img.rotate(90, expand=True)
    img.save(f"rotate_camera_image_{i}.jpg")
