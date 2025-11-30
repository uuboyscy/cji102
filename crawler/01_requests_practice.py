import requests
from bs4 import BeautifulSoup

# Open webpage by requests
url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}
res = requests.get(url, headers=headers)
print(res)

# Get HTML string
html = res.text
# print(html)

# Extract title by BeautifulSoup (a#logo)
# a = 1
# str(a)
# lxml to parse XML
# soup = BeautifulSoup(html, "lxml")
soup = BeautifulSoup(html, "html.parser")

# select() returns a list of Tag
logo_tag_list = soup.select("a#logo")
print(logo_tag_list)
logo_tag = logo_tag_list[0]
print(logo_tag.text)
print("https://www.ptt.cc" + logo_tag["href"])

# select_one returns the first Tag
logo_tag = soup.select_one("a#logo")
print(logo_tag.text)
print("https://www.ptt.cc" + logo_tag["href"])

logo_tag = soup.select_one('a[id="logo"]')
print(logo_tag.text)
print("https://www.ptt.cc" + logo_tag["href"])


logo_tag_list = soup.find_all("a", id="logo")
print(logo_tag_list)
logo_tag = logo_tag_list[0]
print(logo_tag.text)
print("https://www.ptt.cc" + logo_tag["href"])

logo_tag = soup.find("a", id="logo")
print(logo_tag.text)
print("https://www.ptt.cc" + logo_tag["href"])

logo_tag = soup.find("a", {"id": "logo"})
print(logo_tag.text)
print("https://www.ptt.cc" + logo_tag["href"])
