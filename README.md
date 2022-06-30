# Udacity Intermediate Python: Meme Generator

A simple web application that can generate memes.

## How to use the application

These instructions will show you how to run the meme generator app.

### Prerequisites

Before you can run the app, you will need to install some Python modules from `requirements.txt` file.
```bash
pip3 install -r requirements.txt
```
Also, you will need `pdftotext` CLI tool.
```bash
sudo apt install poppler-utils
```

### Running the app
To run the app, you need to execute `app.py` file.
```bash
python3 app.py
```
After that, you can access the app at `https://localhost:5000` and generate memes.

To make a custom meme, you need to run `meme.py` file and provide following arguments:
* --author - author of the meme
* --body - text of the meme
* --path (optional) - image for the meme
```bash
python3 meme.py --author="Jane Doe" --body="Funny meme" --path=<path to a local image file>
