from yaml import load, CLoader as Loader, CDumper as Dumper
import sys

def load_info_file() -> dict:
    with open("info.yaml") as info_file:
        info = load(info_file, Loader=Loader)
    return info

def input_int(prompt: str, *, tries: int = 0, return_none: bool = False) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        if tries >= 2:
            print("Too many tries!")
            if return_none:
                return None
            else:
                sys.exit(-1)
        print("Invalid input")
        return input_int(prompt, tries=tries+1)
