from PIL import Image
SCALE = 0.5
WIDTH = 190
HEIGHT = 166

i = 1
image = Image.open("../assets/character_file_compressed/Monster_move_left.png")
image = image.resize((int(WIDTH * SCALE), int(HEIGHT * SCALE)), Image.ANTIALIAS)
image.save(f"./Monster_move_left.png")
i += 1
image = Image.open("../assets/character_file_compressed/Monster_move_right.png")
image = image.resize((int(WIDTH * SCALE), int(HEIGHT * SCALE)), Image.ANTIALIAS)
image.save(f"./Monster_move_right.png")
i += 1
image = Image.open("../assets/character_file_compressed/Monster_stand_left.png")
image = image.resize((int(WIDTH * SCALE), int(HEIGHT * SCALE)), Image.ANTIALIAS)
image.save(f"./Monster_stand_left.png")
i += 1
image = Image.open("../assets/character_file_compressed/Monster_stand_right.png")
image = image.resize((int(WIDTH * SCALE), int(HEIGHT * SCALE)), Image.ANTIALIAS)
image.save(f"./Monster_stand_right.png")
i += 1
