import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
import os

def get_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.png'):
            images.append(file_path)
    return images

folder_path = "C:/Users/Bennet.Kilian/Downloads/Programming/nanite/"
images = get_images(folder_path)

def parse_filename(filename):
    parts = filename.split("-")
    name = parts[0]
    mission = parts[1]
    pack = parts[2].split(".")[0]
    return name, mission, pack

image_data = []
for image in images:
    name, mission, pack = parse_filename(os.path.basename(image))
    image_data.append({"name": name, "mission": mission, "pack": pack, "path": image})

def filter_images(image_data, name=None, mission=None, pack=None):
    return [img for img in image_data if
            (name is None or img['name'] == name) and
            (mission is None or img['mission'] == mission) and
            (pack is None or img['pack'] == pack)]

filtered_images = filter_images(image_data, name='nanite', mission='m9', pack='rtexture2')
print(filtered_images)

names = set()
missions = set()
packs = set()

for data in filtered_images:
    names.add(data["name"])
    missions.add(data["mission"])
    packs.add(data["pack"])

print("Names: ", names)
print("Missions: ", missions)
print("Packs: ", packs)



