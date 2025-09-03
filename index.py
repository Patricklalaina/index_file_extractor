# ############################ #
#                              #
# By Patrick Randriamanambola  #
#                              #
# ############################ #


import sys
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def download_file(url, filename, curr):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        total_size = int(r.headers.get("content-length", 0))
        chunk_size = 8192  # 8 KB
        des = "file " + str(curr + 1)
        with open(filename, "wb") as f, tqdm(
            total=total_size, unit="B", unit_scale=True, desc=des, ncols=80
        ) as pbar:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))

def process_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
    except:
        print(f"[!] Error for {link}\n[?] Please check filename")
        sys.exit(1)
    soup = BeautifulSoup(response.text, "html.parser")
    vids = soup.find_all("a", attrs={"href": True})
    if not vids:
        print(f"[!] Not found for {link}")
        return None
    file = []
    for vid in vids:
        data = vid["href"]
        frag = data.split(".")
        if len(frag) < 2:
            print(f"{frag} isn't file direct link")
            continue
        file.append(data)
    return file
    
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <link of index website>")
        sys.exit(1)

    link = sys.argv[1]
    # get all filename in current directory
    list_files = os.listdir()

    # /*extract all direct link download in index of/ page*/
    tab = process_link(link)
    # download all link in array [tab]
    
    curr = 0
    for lk in tab:
        # check if files already exist in current directory
        # if 'yes', continue to the next link in array
        if lk in list_files:
            print(f"{lk} already exist!")
            continue
        
        # join href value with link because href value is relative to link
        # ex: link: https://www.fileshare.com/ and href='file.pdf'
        # then complete link = https://www.fileshare.com/file.pdf
        curr_link = link + lk
        try:
            download_file(curr_link, lk, curr)
            curr += 1
        except:
            print(f"Error occured when try link : {curr_link}")
            continue


if __name__ == "__main__":
    main()

