import random
import os
import requests

from flask import Flask, render_template, request
from pathlib import Path

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]
    quotes = []
    for quote_file in quote_files:
        quotes.append(Ingestor.parse(Path(quote_file)))
    images_path = "./_data/photos/dog/"
    imgs = []
    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            imgs.append(Path(images_path) / file)

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    if not request.form.get("image_url"):
        return render_template('meme_form.html')

    image_url = request.form["image_url"]

    try:
        callback = requests.get(image_url, verify=False)
        temp_file = f'./tmp/{random.randint(0,100000000)}.png'
        with open(temp_file, 'wb') as filestream:
            filestream.write(callback.content)

    except Exception:
        return render_template('meme_form.html')

    body = request.form["body"]
    author = request.form["author"]
    path = meme.make_meme(temp_file, body, author)
    Path.unlink(temp_file)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
