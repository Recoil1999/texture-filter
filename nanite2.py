import tkinter as tk
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
    print(name, mission, pack)
    return [img for img in image_data if
            (name is None or img['name'] == name) and
            (mission is None or img['mission'] == mission) and
            (pack is None or img['pack'] == pack)]


folder_path = "C:/Users/Bennet.Kilian/Downloads/Programming/nanite/"
images = get_images(folder_path)

image_data = []
for image in images:
    name, mission, pack = parse_filename(os.path.basename(image))
    image_data.append({"name": name, "mission": mission, "pack": pack, "path": image})



def run(*args):
    name = name_entry.get() if name_entry.get() else None
    mission = mission_entry.get() if mission_entry.get() else None
    pack = pack_entry.get() if pack_entry.get() else None
    filtered_images = filter_images(image_data, name=name, mission=mission, pack=pack)

    result_text.configure(state='normal')
    result_text.delete('1.0', tk.END)
    for img in filtered_images:
        result_text.insert(tk.END, f"{img['name']} - {img['mission']} - {img['pack']}\n")
    result_text.configure(state='disabled')


root = tk.Tk()
root.title("Image Filter")

name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

mission_label = tk.Label(root, text="Mission")
mission_label.grid(row=1, column=0)

mission_entry = tk.Entry(root)
mission_entry.grid(row=1, column=1)

pack_label = tk.Label(root, text="Pack")
pack_label.grid(row=2, column=0)

pack_entry = tk.Entry(root)
pack_entry.grid(row=2, column=1)

run_button = tk.Button(root, text="Run", command=run)
run_button.grid(row=3, column=1, pady=10)

result_label = tk.Label(root, text="Results")
result_label.grid(row=4, column=0, sticky="W")

result_text = tk.Text(root, height=20, width=30, state='disabled')
result_text.grid(row=5, column=0, columnspan=2)

root.mainloop()
