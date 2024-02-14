import pytesseract

from PIL import Image
from typing import BinaryIO


def convert_image_to_text(image_file: BinaryIO) -> str:
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)


def get_text_sections(text: str) -> list[str]:
    return [
        section 
        for section 
        in text.split("\n") 
        if section.strip()
    ]