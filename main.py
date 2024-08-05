data_path="/home/Ubuntu/multidata/"
import os
image_metadata_dict = {}

for file in os.listdir(data_path):
    if file.endswith(".txt"):
        filename = file
        img_path = data_path + file.replace(".txt", ".jpg")
        if os.path.exists(img_path):
            image_metadata_dict[len(image_metadata_dict)] = {
                "filename": filename,
                "img_path": img_path
            }
        else:
            img_path = data_path + file.replace(".txt", ".png")
            if os.path.exists(img_path):
                image_metadata_dict[len(image_metadata_dict)] = {
                    "filename": filename,
                    "img_path": img_path
                }

print(image_metadata_dict)