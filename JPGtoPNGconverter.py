from sys import argv
import os
from PIL import Image

# Function that loops through jpg folder and converts
# and adds to png folder
def loop_pokedex(jpg_folder, png_folder):
    for jpg in os.listdir(jpg_folder):
        img = Image.open(f'{jpg_folder}{jpg}')
        clean_name = os.path.splitext(jpg)[0]
        img.save(f'{png_folder}{clean_name}.png','png')
        print(f"Converted {clean_name}")

def main():
    # grab first and second argument (JPG and PNG folders respectively)
    pokedex = argv[1]
    new = argv[2]

    # check if new/ exists, if not create it
    parent_dir = os.getcwd()
    if not os.path.exists(new):
        os.mkdir(new)

    # loop through Pokedex
    # convert images to png
    # save to the new folder
    loop_pokedex(pokedex, new)

if __name__ == "__main__":
    main()