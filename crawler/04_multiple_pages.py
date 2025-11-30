from pathlib import Path

import requests
from bs4 import BeautifulSoup

from crawler_utility import extract_article

folder_path = Path("./ptt_gossiping")
folder_path.mkdir(parents=True, exist_ok=True)

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}
cookies = {
    "over18": "1",
}

for _ in range(5):
    res = requests.get(url, headers=headers, cookies=cookies)

    html = res.text

    soup = BeautifulSoup(html, "html.parser")

    title_tag_list = soup.select("div.title")

    for title_tag in title_tag_list:
        title_a_tag = title_tag.select_one("a")
        # title_a_tag may be None
        if title_a_tag is None:
            continue
        title_str = title_a_tag.text
        article_url_str = "https://www.ptt.cc" + title_a_tag["href"]
        # Extract article
        article_str = extract_article(article_url_str)

        abnormal_str_list = ["?", "#", "*", ":", "+", "=", "/"]
        for abnormal_str in abnormal_str_list:
            title_str = title_str.replace(abnormal_str, "_")
        article_file_path = folder_path / f"{title_str}.txt"

        with article_file_path.open("w") as f:
            f.write(article_str)

        # print(title_a_tag)
        print("Title:", title_str)
        print("Article URL:", article_url_str)
        print("Article:", article_str)
        print("==========")

    # Get new URL, and assign to url
    """
    <a class="btn wide" href="/bbs/Gossiping/index38886.html">‹ 上頁</a>
    """
    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
    print(url)
