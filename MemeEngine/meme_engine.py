from pathlib import Path
from PIL import Image, ImageDraw
from random import randint


__all__ = ["MemeEngine"]


class MemeEngine:
    """Engine for generating memes."""

    def __init__(self, output_dir):
        """ Save and create the output directory path """
        self.output_dir = Path(output_dir)
        if not self.output_dir.is_dir():
            self.output_dir.mkdir()

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate a new meme with provided info."""
        meme_output = Path(f"{self.output_dir}/meme_{randint(0, 5000)}.png")
        if width >= 500:
            width = 500

        try:
            print(f"imedz path = {img_path}")
            with Image.open(Path(img_path)) as image:
                ratio = image.height / image.width
                height = width * ratio
                image = image.resize((int(width), int(height)))
                font_size = int(image.height/30)
                image_draw = ImageDraw.Draw(image)
                x_position = randint(0, int(image.width/4))
                y_position = randint(0, int(image.height-font_size*2))
                image_draw.text((x_position, y_position), text)
                image_draw.text((int(x_position*1.5), y_position+font_size), f" - {author}")
                image.save(meme_output)

        except Exception:
            raise FileNotFoundError(f"File {str(img_path)} cannot be found.")
        return meme_output
