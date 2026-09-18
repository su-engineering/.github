"""Render the organization banner from the original ASCII wordmark."""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--font", required=True, help="Path to JetBrains Mono Regular TTF")
args = parser.parse_args()

SCALE = 2
image = Image.new("RGB", (1200 * SCALE, 340 * SCALE), "#10110f")
draw = ImageDraw.Draw(image)


def text(position, value, size, color):
    font = ImageFont.truetype(args.font, size * SCALE)
    draw.text(tuple(p * SCALE for p in position), value, font=font, fill=color)


def line(start, end, color):
    draw.line(tuple(p * SCALE for p in (*start, *end)), fill=color, width=SCALE)


text((48, 28), "SU / ENGINEERING", 13, "#aaa79d")
text((938, 28), "BILBAO / BASQUE COUNTRY", 13, "#aaa79d")
line((48, 63), (1152, 63), "#4d4c43")

wordmark = [
    "                       _                 _",
    " ___ _ _   ___ ___ ___|_|___ ___ ___ ___|_|___ ___",
    "|_ -| | |_| -_|   | . | |   | -_| -_|  _| |   | . |",
    "|___|___|_|___|_|_|_  |_|_|_|___|___|_| |_|_|_|_  |",
    "                  |___|                       |___|",
]
for row, value in enumerate(wordmark):
    text((48, 85 + row * 29), value, 29, "#eeeade")

line((48, 265), (1152, 265), "#4d4c43")
text((48, 286), "water. fire. code.", 18, "#ff6538")
text((666, 289), "identity. privacy. products + projects.", 16, "#aaa79d")

output = Path(__file__).resolve().parents[1] / "assets" / "banner.png"
output.parent.mkdir(parents=True, exist_ok=True)
image.save(output, optimize=True)
print(output)
