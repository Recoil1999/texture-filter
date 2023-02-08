import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


def get_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.png'):
            images.append(file_path)
    return images


def parse_filename(filename):
    parts = filename.split("-")
    name = parts[0]
    mission = parts[1]
    pack = parts[2].split(".")[0]
    return name, mission, pack


def filter_images(image_data, name=None, mission=None, pack=None):
    return [img for img in image_data if
            (name is None or img['name'] == name) and
            (mission is None or img['mission'] == mission) and
            (pack is None or img['pack'] == pack)]


def run(*args):
    name = name_combobox.get() if name_combobox.get() else None
    mission = mission_combobox.get() if mission_combobox.get() else None
    pack = pack_combobox.get() if pack_combobox.get() else None
    filtered_images = filter_images(image_data, name=name, mission=mission, pack=pack)
    result_text.configure(state='normal')
    result_text.delete('1.0', tk.END)
    for img in filtered_images:
        result_text.insert(tk.END, f"{img['name']} - {img['mission']} - {img['pack']}\n")
    result_text.configure(state='disabled')


folder_path = "C:/Users/Bennet.Kilian/Downloads/Programming/nanite/"
images = get_images(folder_path)

image_data = []
for image in images:
    name, mission, pack = parse_filename(os.path.basename(image))
    image_data.append({"name": name, "mission": mission, "pack": pack, "path": image})


names = set()
missions = set()
packs = set()

for data in image_data:
    names.add(data["name"])
    missions.add(data["mission"])
    packs.add(data["pack"])



root = tk.Tk()
root.title("Image Filter")

names = list(names)
names.insert(0, "")
names.sort()
missions = list(missions)
missions.insert(0, "")
missions.sort()
packs = list(packs)
packs.insert(0, "")
packs.sort()

# Name combobox
name_options = names
name_combobox = ttk.Combobox(root, values=name_options)
name_combobox.current(0)
# name_combobox.bind("<<ComboboxSelected>>", on_name_change)
name_combobox.grid(row=0, column=0)

# Mission combobox
mission_options = missions
mission_combobox = ttk.Combobox(root, values=mission_options)
mission_combobox.current(0)
# mission_combobox.bind("<<ComboboxSelected>>", on_mission_change)
mission_combobox.grid(row=1, column=0)

# Pack combobox
pack_options = packs
pack_combobox = ttk.Combobox(root, values=pack_options)
pack_combobox.current(0)
# pack_combobox.bind("<<ComboboxSelected>>", on_pack_change)
pack_combobox.grid(row=2, column=0)

run_button = tk.Button(root, text="Run", command=run)
run_button.grid(row=3, column=1, pady=10)

result_label = tk.Label(root, text="Results")
result_label.grid(row=4, column=0, sticky="W")

result_text = tk.Text(root, height=20, width=30, state='disabled')
result_text.grid(row=5, column=0, columnspan=2)

root.mainloop()