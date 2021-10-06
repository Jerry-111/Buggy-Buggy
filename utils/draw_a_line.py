from PIL import Image, ImageDraw
#
img = Image.open("../assets/backgrounds/background_1.jpg")
img = Image.open("/Users/victor/PycharmProjects/some-2d-shooting-game/assets/backgrounds/background_1.jpg")
draw = ImageDraw.Draw(img)
# draw.line()

for i in range(18):
    for j in range(12):
        draw.line((384*i/12, 576*j/18, 384*i/12, 576*j/18+32), fill=128)
        draw.line((384*i/12, 576*j/18, 384*i/12+32, 576*j/18), fill=128)

img.show("/Users/victor/PycharmProjects/some-2d-shooting-game/assets/backgrounds/background_1.jpg")