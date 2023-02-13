import json

# Open the file
with open('C:\\Users\\Bennet.Kilian\\Downloads\\Programming\\Div\\RecoilTextures-main\\png\\atlas.json', 'r') as json_file:
    # Use json.load to parse the JSON data from the file
    data = json.load(json_file)

resolutions = set()
pixel_count = set()

for files in data:
    for items in data[files]:
        resolutions.add(f'{items["width"]} x {items["height"]}')
        pixel_count.add(f'{items["width"] * items["height"]} - {items["width"] + items["height"]}')

for pixel_counts in pixel_count:
    print(pixel_counts)
