from minio import Minio
from PIL import Image, ImageDraw
import random

SIZE = 5
MINIO_USER = "Sk1B1D33"
MINIO_PASSWORD = "T01L3T-S4N"
WIDTH = 1920
HEIGHT = 1080

client = Minio(
    "minio:9000",
    access_key=MINIO_USER,  
    secret_key= MINIO_PASSWORD,
    secure=False
)

bucket_name = "my-bucket"
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

image = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

n = 0
err_count = 0
while True:
    for x in range(0, WIDTH, SIZE):
        for y in range(0, HEIGHT, SIZE):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.rectangle([x, y, x + SIZE, y + SIZE], fill=color)

    fn = f"random_colors_{n}.jpg"
    image.save(fn, "JPEG")
    try:
        client.fput_object(
            bucket_name,
            fn,
            fn,
            content_type="image/jpeg"
        )
    except Exception as err:
        print(f"ResponseError occurred: {err}")
        err_count += 1
        if err_count == 5:
            break
        continue

    n += 1
