import tkinter as tk
from tkinter import ttk

def on_name_change(*args):
    print("Name changed to:", name_combobox.get())
    selected_name = name_combobox.get()
    if selected_name == "John":
        mission_combobox['values'] = ["Explore", "Discover"]
    else:
        mission_combobox['values'] = ["Explore", "Discover", "Study", "Research"]

def on_mission_change(*args):
    print("Mission changed to:", mission_combobox.get())

def on_pack_change(*args):
    print("Pack changed to:", pack_combobox.get())

root = tk.Tk()

# Name combobox
name_options = ["John", "Jane", "Jim", "Jill"]
name_combobox = ttk.Combobox(root, values=name_options)
name_combobox.current(0)
name_combobox.bind("<<ComboboxSelected>>", on_name_change)
name_combobox.pack()

# Mission combobox
mission_options = ["Explore", "Discover", "Study", "Research"]
mission_combobox = ttk.Combobox(root, values=mission_options)
mission_combobox.current(0)
mission_combobox.bind("<<ComboboxSelected>>", on_mission_change)
mission_combobox.pack()

# Pack combobox
pack_options = ["Food", "Clothing", "Tools", "Equipment"]
pack_combobox = ttk.Combobox(root, values=pack_options)
pack_combobox.current(0)
pack_combobox.bind("<<ComboboxSelected>>", on_pack_change)
pack_combobox.pack()

print("Initial name:", name_combobox.get())
print("Initial mission:", mission_combobox.get())
print("Initial pack:", pack_combobox.get())
root.mainloop()
