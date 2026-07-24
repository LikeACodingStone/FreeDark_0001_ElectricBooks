'''
1. This is a python code file, cycle reading all the list names in file "NewReadingBooks.txt" in current code same folder.
inside the move list could be like fellowing
'
电影 Book name A
Book name B
Book name C
'
while one name was been read, moving to the updating process from 2 - 7. until finished updating, move back to here, read the next 
movie inside the files. after reading and updated all the movie lists. delete the movie name that updating successfully. 
keep the movie that updating failed. if all success, clear this file, but do not delete.

2. acknowledge this function is for updating infomation to the book list, always do no change the original file content, 
only add content list to the existing list.

3. the content inside the list is like the fellowing.
'
| Name  | Author | Summary  |
| --- | --- | ---| 
| 古拉格群岛 | 索尔仁尼琴 | 历史学家亚历山大·索尔仁尼琴所编著的一部反映苏联强制劳动和集中营生活全貌的非虚构作品，共三卷 |
| 耳语者| 奥兰多·费吉斯 | 其一系列解读沙俄及苏联历史的著作《耳语者：斯大林时代苏联的私人生活》 |
'
means via the new book name generate a new line add to the bottom. 
7. Regarding fill the book list, please search in the wiki, 
please summarize all the content in 60 chinese 汉字

'''

'''
1. Please refer to the logs and code fix the two bugs.
BUG A. please do not change the original existing list inside BookList.md
BUG B. please always remember to extract the Author and fill to the table 
'''
import os
import requests
import re
import urllib.parse

BOOK_LIST_FILE = "BookList.md"
NEW_READING_FILE = "NewReadingBooks.txt"

WIKI_API = "https://zh.wikipedia.org/w/api.php"
GOOGLE_API = "https://www.googleapis.com/books/v1/volumes"

HEADERS = {
    "User-Agent": "BookUpdater/4.0"
}


# ================= WIKI =================

def search_wiki(book_name):
    params = {
        "action": "query",
        "list": "search",
        "format": "json",
        "srsearch": f'intitle:{book_name}'
    }

    try:
        r = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=10)
        data = r.json()
        results = data.get("query", {}).get("search", [])
        if not results:
            return None, None
        return results[0]["pageid"], results[0]["title"]
    except:
        return None, None


def get_wiki_wikitext(pageid):
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "format": "json",
        "pageids": pageid
    }

    r = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=10)
    data = r.json()
    page = data["query"]["pages"][str(pageid)]
    return page["revisions"][0]["slots"]["main"]["*"]


def extract_author_from_wikitext(text):
    patterns = [
        r"\|\s*作者\s*=\s*(.+)",
        r"\|\s*author\s*=\s*(.+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            author = match.group(1)
            author = re.sub(r"\[\[|\]\]", "", author)
            author = re.sub(r"<.*?>", "", author)
            return author.strip()[:30]

    return None


def get_wiki_summary(title):
    encoded_title = urllib.parse.quote(title)
    url = f"https://zh.wikipedia.org/api/rest_v1/page/summary/{encoded_title}"

    r = requests.get(url, headers=HEADERS, timeout=10)
    if r.status_code != 200:
        return None

    data = r.json()
    summary = data.get("extract", "").replace("\n", "")
    return summary[:60]


# ================= GOOGLE BOOKS =================

def search_google_books(book_name):
    params = {
        "q": book_name,
        "maxResults": 1,
        "langRestrict": "zh"
    }

    try:
        r = requests.get(GOOGLE_API, params=params, timeout=10)
        data = r.json()

        items = data.get("items")
        if not items:
            return None, None

        info = items[0]["volumeInfo"]

        authors = info.get("authors", ["未知"])
        author = ", ".join(authors)

        summary = info.get("description", "")
        summary = re.sub(r"<.*?>", "", summary)
        summary = summary.replace("\n", "")
        summary = summary[:60]

        return author, summary if summary else "暂无简介"

    except:
        return None, None


# ================= 写入 =================

def append_book(name, author, summary):
    file_exists = os.path.exists(BOOK_LIST_FILE)

    with open(BOOK_LIST_FILE, "a", encoding="utf-8") as f:
        if not file_exists or os.stat(BOOK_LIST_FILE).st_size == 0:
            f.write("| Name | Author | Summary |\n")
            f.write("| --- | --- | --- |\n")

        f.write(f"| {name} | {author} | {summary} |\n")


# ================= 主逻辑 =================

def main():
    if not os.path.exists(NEW_READING_FILE):
        print("NewReadingBooks.txt 不存在")
        return

    with open(NEW_READING_FILE, "r", encoding="utf-8") as f:
        books = [line.strip() for line in f if line.strip()]

    failed = []

    for book in books:
        print("处理:", book)

        # 先 Wiki
        pageid, title = search_wiki(book)

        if pageid:
            try:
                wikitext = get_wiki_wikitext(pageid)
                author = extract_author_from_wikitext(wikitext)
                summary = get_wiki_summary(title)

                if author and summary:
                    append_book(book, author, summary)
                    print("✔ Wiki 成功")
                    continue
            except:
                pass

        # Wiki 失败 → Google Books
        author, summary = search_google_books(book)

        if author and summary:
            append_book(book, author, summary)
            print("✔ Google Books 成功")
        else:
            print("✘ 全部失败")
            failed.append(book)

    # 写回失败列表
    with open(NEW_READING_FILE, "w", encoding="utf-8") as f:
        for book in failed:
            f.write(book + "\n")

    print("全部完成")


if __name__ == "__main__":
    main()
