# Tibame 20251109 pyetl morning

## Overview
- Highlighted how to capture lectures: record audio, feed transcripts into AI tools (e.g., Notebook LM) for post-class notes, but still hand-write code yourself before asking AI for reviews.
- Revisited HTML fundamentals so that crawler targets are readable: tags nest to form a tree, repeated UI blocks (like PTT titles) share identical structures, and indentation only improves readability.
- Practiced scanning PTT pages with browser devtools to locate article titles, links, and metadata, paying attention to nearest unique parents (e.g., `div.title > a`).
- Explained why servers often return relative paths; the browser knows the host, so crawlers must prepend the domain when necessary.

## Selecting Elements Reliably
- Start from the content you want (e.g., an `<a>` tag) and walk outward until you encounter a unique combination of tag and attributes (class/id) that only wraps the desired records.
- Translate that structure into CSS selectors such as `div.title > a` or `div.r-ent div.title`, then feed it to BeautifulSoup’s `.select()` / `.find_all()` to receive a list.
- Remember that attributes like `class` map to `.` in selectors and multi-class nodes become `div.r-ent.some-class.other-class`.
- After grabbing each element, strip HTML tags to keep only text/URLs; loop through the resulting list just like any other iterable.

## Workflow For Scrapers
1. Use devtools → Elements to understand the DOM and confirm repeated patterns.
2. Capture the request (Network tab) so you know the exact URL, method, and headers the browser used.
3. Recreate the request with `requests.get`, check `response.text`, and give that HTML to BeautifulSoup.
4. Iterate over the parsed nodes, clean fields, and store them (printing, writing CSV, etc.).

## Practice Notes
- Build tiny static HTML files (e.g., `index.html`) locally to experiment with tags before scraping.
- Keep project environments handy so you can spin up a new scraper project quickly; this becomes important for interviews/demos.
- Later the same HTML knowledge will transfer to exposing local files via a Python web framework (transcript called it "Flex", i.e., Flask) so others can access your output.
