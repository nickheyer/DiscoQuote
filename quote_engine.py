import subscene
import sys
import os

def get_root():
    return os.path.dirname(__file__)


def get_title():
    title = None
    if len(sys.argv) == 1:
        title = input("What is the title you would like a random quote from?")
    else:
        title = sys.argv[1]
    

def search(title):
    sub_link = subscene.sel_title(name = title.replace(" ", "-"))
    if sub_link: #If title exists in subscene
        sub = subscene.sel_sub(page=sub_link, sub_count=1, name=title)
        return sub
    else:
        raise Exception("Title not found")


def download_sub(sub):
    subscene.dl_sub(sub)

def main():
    
    s = search("Doctor Strange")
    download_sub(s)
    
    return


if __name__ == "__main__":
    main()