# Python ETL｜爬蟲與 Selenium 實務（2025/11/30）

## PTT 文章擷取流程
- 先用 `requests` 抓頁面，`BeautifulSoup` 取 `#main-content`，先 `print` 檢查內容再做清洗。
- `select` 目標標籤後 `.extract()` 移除不需要的元素（作者 `div.article-meta-line`、推文 `span.push` 等），最後 `.get_text()` 拿純文字。
- 說明 DOM/樹狀結構：`.extract()` 直接修改原樹，子節點被移除後，父節點內容同步消失。

## 資料存檔
- 用 `pathlib.Path` 組路徑並建資料夾：`Path("PTT_Joke").mkdir(parents=True, exist_ok=True)`。
- 每篇文章以標題命名 `.txt`，路徑以 `Path` 串接，寫入乾淨內文。

## Selenium 入門與反爬處理
- Selenium Manager 會自動下載對應 ChromeDriver，通常不用手動指定 driver。
- 若頁面需 Cookie/動態載入：先用 Selenium 取得 Cookie，再用 `requests` 搭配 Cookie 抓取，速度勝過全程 Selenium。
- PTT 八卦版示範：先進站拿 Cookie，再抓列表；展示被驗證碼攔截的情況，提到下次示範更能避開防爬的工具。

## 其他補充
- Coding test 心態：多數公司重視解題思路，可寫 pseudo code；建議練常見資料結構/演算法題。
- 練習資源：LeetCode Pandas/SQL 分類可熟悉資料處理，推薦同題分別用 Pandas 與 SQL 嘗試。
