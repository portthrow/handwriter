import os
from glob import glob
from PIL import Image

class _page_info():
    x_marker = 0
    y_marker = 0
    page_count = 0
    character_height = 0
    character_width = 0
    page_width = 0
    page_height = 0
    page = False


def map_images():
    punctuation = ".,'\"!@#$%^&*()<>?{}-_:;|/[]`~\\"
    character_map = dict()
    for char in glob("images/*.png"):
        character = os.path.split(char)[-1]
        if "_" in character:
            character = character.lower().replace('_','')
        elif "punc" in character:
            index = os.path.splitext(character)[0].replace("punc","")
            index = int(index)
            character = punctuation[index]
        character = os.path.splitext(character)[0]
        tmp = Image.open(char)
        tmp.convert('RGBA')
        character_map[character] = tmp
    return character_map


def read_content():
    with open("./content.txt", "r") as f:
        data = f.read()
    return data


def make_page(page_info):
    return Image.new('RGBA', (page_info.page_width, page_info.page_height))


# A normal page at size-12 font is 92 characters wide and 49 lines deep
def init_page_info(character_map):
    page_info = _page_info()
    page_info.character_width = character_map['a'].width
    page_info.character_height = character_map['a'].height
    page_info.page_width  = page_info.character_width * 92
    page_info.page_height = page_info.character_height * 49
    page_info.page = make_page(page_info)
    return page_info


def check_page(page_info, model):
    page_info.x_marker += model.width
    if page_info.x_marker >= page_info.page_width:
        page_info.x_marker = 0
        page_info.y_marker += model.height
    if page_info.y_marker >= page_info.page_height:
        page_info.y_marker = 0
        save_page(page_info)
        page_info.page = make_page(page_info)


def save_page(page_info):
    page_info.page_count += 1
    page_info.page.save("page%s.png" % page_info.page_count)
        

def write_image(data, character_map):
    page_info = init_page_info(character_map)
    for char in data:
        # Handle special cases first
        if char == "\t":
            char = " "
        elif char == "\r":
            continue
        elif char == "\n":
            page_info.y_marker += page_info.character_height
            check_page(page_info, character_map[" "])
            page_info.x_marker = 0
            continue
        model = character_map[char]
        page_info.page.paste(model, (page_info.x_marker, page_info.y_marker))
        check_page(page_info, model)
    save_page(page_info)


if __name__ == '__main__':
    character_map = map_images()
    data = read_content()
    write_image(data, character_map)
