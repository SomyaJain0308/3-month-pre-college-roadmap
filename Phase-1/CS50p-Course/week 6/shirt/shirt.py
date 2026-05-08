import sys
import csv
from PIL import Image
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".jpg") and not sys.argv[2].endswith(".jpg"):
    sys.exit("Invalid input")
elif not sys.argv[1].endswith(".jpeg") and not sys.argv[2].endswith(".jpeg"):
    sys.exit("Invalid input")
elif not sys.argv[1].endswith(".png") and not sys.argv[2].endswith(".png"):
    sys.exit("Invalid input")
images = []
with Image.open(sys.argv[1]) as im:
    im.show()
