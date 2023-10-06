import feedparser
import re

def main():
    position = -1
    opened = True
    frstOldLine = ""
    url = "https://cc.cz/feed/"

    d = feedparser.parse(url)
    
    if d.status != 200:
        return print("An error has occured.")

    try:
        with open('rss.txt', 'r') as f:
            frstOldLine = re.sub(r'.*: |\n','',f.readline(-1))
    except OSError:
        opened = False

    itemField = [i for i in d.entries]

    with open('rss.txt', 'w') as f:
        for index, i in enumerate(itemField):
            if frstOldLine == i.title:
                position = index
            f.write(f"{index+1}: {i.title}\n")
            f.write(f"{' '*4}- {i.link}\n")
            desc = re.sub(r'<img.* />|<p>Článek.*/p>|<p>|</p>',r'',i.description)
            f.write(f"{' '*4}- {desc}\n")
            f.write("\n")
        
    print("\nDone!")

    if opened:
        if position == 0:
            print("No new news found.")
        elif position == -1:
            print(f"Found {len(d)} new news!")
        else:
            print(f"Found {position} new news!")
            
    print(f"Fetched {len(itemField)} news.\n")
    
if __name__ == "__main__":
    main()
