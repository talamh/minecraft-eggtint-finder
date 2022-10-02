# colored images can be found in the Resource Pack Template:
# https://aka.ms/resourcepacktemplate
import io
import os.path
import zipfile
from typing import Tuple

from PIL.Image import open as ImageOpen
from downloader import download


def find_pixel_tint(pixel: Tuple[int, int], grey_value: int) -> int:
    red = int(round((255 * pixel[0]) / grey_value))
    green = int(round((255 * pixel[1]) / grey_value))
    blue = int(round((255 * pixel[2]) / grey_value))

    return (red << 16) | (green << 8) | blue


def find_tints(filename: str) -> Tuple[str, str]:
    # egg_glow_squid.png has a palette, so we just convert all egg images to RGB
    image = ImageOpen(io.BytesIO(archive.read(filename))).convert('RGB')
    body_color = find_pixel_tint(image.getpixel((8, 8)), 0xdb)
    overlay_color = find_pixel_tint(image.getpixel((5, 9)), 0xe2)

    return f'{hex(body_color).replace("0x", "")}'.zfill(6), \
           f'{hex(overlay_color).replace("0x", "")}'.zfill(6)


if __name__ == '__main__':
    if os.path.exists('./cache/resourcepacktemplate'):
        with zipfile.ZipFile('./cache/resourcepacktemplate') as archive:
            for f in archive.namelist():
                if 'egg_' in f and '_egg_' not in f and f.split('.')[1] not in ['fsb', 'pdn']:
                    body, overlay = find_tints(f)

                    # pylint: disable=line-too-long
                    tint_string = f'(spawn_egg.png^[multiply:#{body})^(spawn_egg_overlay.png^[multiply:#{overlay})'

                    print(f'{f} "{tint_string}"')
    else:
        download(urls=["https://aka.ms/resourcepacktemplate"], dest_dir="cache/")
