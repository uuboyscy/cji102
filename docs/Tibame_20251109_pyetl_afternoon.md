# Tibame 20251109 pyetl afternoon

## DevTools And HTTP Essentials
- Reopened the browser’s developer tools (F12 / Cmd+Opt+I) and reviewed how the Network panel records every request as soon as the page reloads.
- Read each entry from top to bottom: request URL, HTTP method (GET in the demo), status codes (2xx success, 3xx redirects, 4xx/5xx failures) and rate-limit codes like 429.
- Pointed out that response bodies, headers, and timing breakdowns matter mostly for debugging, but crawlers at minimum must copy the method, URL, and any auth headers.

## Cookies And Session State
- Used PTT Gossiping as an example: once you confirm you are 18, the server sets `over18=1` in the `Cookie` header.
- Every subsequent request automatically includes that cookie, letting the site skip the prompt; crawlers must mimic the same cookie to bypass the age gate.

## Reverse-Engineering Query Parameters
- Watched the request URL to see query strings such as `?q=keyword` and experimented by editing those values directly in the address bar.
- Verified which parameters were optional by deleting them and observing whether the results changed; keeping the URL minimal makes code easier to maintain.
- Converted the working URL into a Python string template (using `format`, f-strings, or `%s`) so loops can substitute multiple keywords.

## Coding The Crawler
1. Define the endpoint template and desired keyword list.
2. For each keyword, `requests.get` the rendered URL, passing along mandatory headers/cookies captured earlier.
3. Feed the HTML to BeautifulSoup, `select` the repeated blocks (e.g., `div.title > a`), and extract text/links.
4. Append structured data to a list/CSV/database for later analysis.

## Tips Shared In Class
- Always reload the page with Network tab already open so the initial document request is captured.
- Keep an eye on payload tabs for POST requests; the same structure must be recreated in code.
- Rate limits (HTTP 429) hint that you need delays or API keys—log them rather than retrying blindly.
