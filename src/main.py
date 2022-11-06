import eel
import random

eel.init("web")

def main():
    eel.start("index.html",
              size=(1080, 720),
              mode="chrome",
              cmdline_args=["--disable-extensions"]
              )

if __name__ == "__main__":
    main()