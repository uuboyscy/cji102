import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}

def extract_article(article_url_str: str) -> str:
    res = requests.get(article_url_str, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    article_tag = soup.select_one("#main-content")

    # Get all tags that we don't need
    span_tag_list = article_tag.select("span")

    # Extract such tags so the tags will be removed
    for span_tag in span_tag_list:
        span_tag.extract()

    return article_tag.text

if __name__ == "__main__":
    article_url_str = "https://www.ptt.cc/bbs/joke/M.1764291976.A.38C.html"
    article_str = extract_article(article_url_str)
    print(article_str)
