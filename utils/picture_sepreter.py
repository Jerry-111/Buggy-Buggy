from PIL import Image

img = Image.open("../assets/resource_file.png")
print(img.size)

for i in range(8):
    for j in range(3):
        cropped = img.crop((i*32, j*32, (i+1)*32, (j+1)*32))  # (left, upper, right, lower)
        cropped.save(f"../assets/resources/picture-{i,j}.png")