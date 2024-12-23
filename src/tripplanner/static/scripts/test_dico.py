from pathlib import Path

icons = Path.cwd() / "src" / "vla_django" / "static" / "icons"
pictures = {}

for icon in icons.glob("*"):
    if icon.is_file():
        # print(icon.name)
        pictures[icon.stem] = icon.name

print(pictures)

pic_list = list(pictures.keys())

for el in pic_list:
    print(f"• {el} (longueur : {len(el)} caractères)")
