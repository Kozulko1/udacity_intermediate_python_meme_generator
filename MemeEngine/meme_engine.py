from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from random import randint


__all__ = ["MemeEngine"]


class MemeEngine:
    """Engine for generating memes."""

    def __init__(self, output_dir):
        """Save and create the output directory path"""
        self.output_dir = Path(output_dir)
        if not self.output_dir.is_dir():
            self.output_dir.mkdir()

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate a new meme with provided info."""
        meme_output = Path(f"{self.output_dir}/meme_{randint(0, 5000)}.png")
        if width >= 500:
            width = 500

        try:
            with Image.open(Path(img_path)) as image:
                ratio = image.height / image.width
                height = width * ratio
                image = image.resize((int(width), int(height)))
                image_draw = ImageDraw.Draw(image)
                image_draw.text((100, 100), text)
                image_draw.text((200, 200), f" - {author}")
                image.save(meme_output)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {str(img_path)} cannot be found.")
        return meme_output
