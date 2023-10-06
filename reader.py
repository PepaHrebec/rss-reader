import feedparser
import re

def main():
    position = 0
    opened = True
    titles = []
    url = "https://cc.cz/feed/"

    d = feedparser.parse(url)
    
    if d.status != 200:
        return print("An error has occured.")

    try:
        with open('rss.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if re.match("\d", line):
                    titles.append(re.sub(r'.*: |\n','',line))
    except OSError:
        opened = False

    itemField = [i for i in d.entries]

    with open('rss.txt', 'w') as f:
        for index, i in enumerate(itemField):
            if index == 0:
                try:
                    position = titles.index(i.title) 
                    # position 0
                except ValueError:
                    pass
            f.write(f"{index+1}: {i.title}\n")
            f.write(f"{' '*4}- {i.link}\n")
            desc = re.sub(r'<img.* />|<p>Článek.*/p>|<p>|</p>',r'',i.description)
            f.write(f"{' '*4}- {desc}\n")
            f.write("\n")
        
    print("\nDone!")

    if opened:
        if position <= 0:
            print("No new news found.")
        else:
            print(f"Found {position} new news!")
            
    print(f"Fetched {len(itemField)} news.\n")
    
if __name__ == "__main__":
    main()
