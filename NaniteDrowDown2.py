import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from functools import partial
import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


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
    tpack = parts[2].split(".")[0]
    return name, mission, tpack


def filter_images(image_data, name=None, mission=None, tpack=None):
    return [img for img in image_data if
            (name is None or img['name'] == name) and
            (mission is None or img['mission'] == mission) and
            (tpack is None or img['tpack'] == tpack)]


def clear_combobox(current_combobox):
    current_combobox.set("")
    run()


def display_images(image_objects):
    tk_images = []
    for widget in root.winfo_children():
        widget_row = widget.grid_info()["row"]
        if widget_row >= 2:
            widget.destroy()
    for i, image2 in enumerate(image_objects):
        i = i + 6
        tk_image = ImageTk.PhotoImage(image2)
        tk_images.append(tk_image)
        label = tk.Label(root, image=tk_image, width=64, height=64, anchor="center")
        # Label must be stored as an instance variable, so that it is not garbage collected
        label.image = tk_image
        label.grid(row=i // 3, column=i % 3)

def run(*args):
    image_objects = []
    name = name_combobox.get() if name_combobox.get() else None
    mission = mission_combobox.get() if mission_combobox.get() else None
    tpack = tpack_combobox.get() if tpack_combobox.get() else None
    filtered_images = filter_images(image_data, name=name, mission=mission, tpack=tpack)
    for image in filtered_images:
        image_objects.append(Image.open(image["path"]))
    display_images(image_objects)
    # result_text.configure(state='normal')
    # result_text.delete('1.0', tk.END)
    # for img in filtered_images:
    #     result_text.insert(tk.END, f"{img['name']} - {img['mission']} - {img['tpack']}\n")
    # result_text.configure(state='disabled')


folder_path = "C:\\Users\\Bennet\\Downloads\\nanite"
images = get_images(folder_path)

image_data = []
for image in images:
    name, mission, tpack = parse_filename(os.path.basename(image))
    image_data.append({"name": name, "mission": mission, "tpack": tpack, "path": image})
    # image_objects.append(Image.open(image))

image_data = sorted(image_data, key=lambda x: natural_keys(x["mission"]))

names = set()
missions = set()
tpacks = set()

for data in image_data:
    names.add(data["name"])
    missions.add(data["mission"])
    tpacks.add(data["tpack"])

root = tk.Tk()
root.geometry("430x700")
root.title("Image Filter")

names = list(names)
# names.insert(0, "")
names.sort()
missions = list(missions)
# missions.insert(0, "")
missions.sort(key=natural_keys)
tpacks = list(tpacks)
# tpacks.insert(0, "")
tpacks.sort()

# Name combobox
name_options = names
name_combobox = ttk.Combobox(root, values=name_options)
name_combobox.set("")
name_combobox.bind("<<ComboboxSelected>>", run)
name_combobox.grid(row=0, column=0)

# Clear Name Button
clear_name_button = tk.Button(root, text="Clear", command=partial(clear_combobox, name_combobox))
clear_name_button.grid(row=1, column=0)

# Mission combobox
mission_options = missions
mission_combobox = ttk.Combobox(root, values=mission_options)
mission_combobox.set("")
mission_combobox.bind("<<ComboboxSelected>>", run)
mission_combobox.grid(row=0, column=1)

# Clear Mission Button
clear_mission_button = tk.Button(root, text="Clear", command=partial(clear_combobox, mission_combobox))
clear_mission_button.grid(row=1, column=1)

# tpack combobox
tpack_options = tpacks
tpack_combobox = ttk.Combobox(root, values=tpack_options)
tpack_combobox.set("")
tpack_combobox.bind("<<ComboboxSelected>>", run)
tpack_combobox.grid(row=0, column=2)

# Clear Pack Button
clear_tpack_button = tk.Button(root, text="Clear", command=partial(clear_combobox, tpack_combobox))
clear_tpack_button.grid(row=1, column=2)

# def testing():
#     result_label = tk.Label(root, text="Results")
#     result_label.grid(row=2, column=0, pady=10, sticky="W")

# result_text = tk.Text(root, height=20, width=30, state='disabled')
# result_text.grid(row=3, column=0, columnspan=2)

# testing()
run()
root.mainloop()
