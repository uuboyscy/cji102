import requests

# Open webpage by requests
url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}
res = requests.get(url, headers=headers)
print(res)

# Get HTML string

# Extract title by BeautifulSoup (a#logo)
