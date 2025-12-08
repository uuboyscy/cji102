# Tibame 20251206 pyetl morning

- Selenium 爬蟲：示範用一般 Selenium 無法穩定爬取 Dcard，改用 `undetected-chromedriver`；唯一差異是 `from undetected_chromedriver import Chrome`，其餘程式不變。說明常見 options（headless、no-sandbox、disable-dev-shm-usage、user-agent、自動最大化）與用途。
- 無限捲動：透過 `execute_script("window.scrollTo(0, document.body.scrollHeight)")` 反覆向下滾動並暫停，再向上滾動，取得完整的 HTML 後改用 BeautifulSoup 離線解析，以降低被反爬機率。
- 例外處理：Windows 上 `undetected-chromedriver` 偶發 WinError 6（quit 邏輯瑕疵）；可自訂繼承原本 Chrome 類別，覆寫 `quit/close`，並以 try/except 吸收 OS error；若不想動原始碼可暫時退回標準 Selenium Chrome 但成功率較低。
- Pandas/Jupyter 基礎：安裝 `pandas`、`jupyter`；核心物件為 DataFrame/Series。回顧 filter、多條件 AND/OR、`apply`、`groupby`、`merge`/`join`、儲存為 CSV/JSON/Parquet。解釋欄式儲存（Parquet）在壓縮與查詢上的效益。
- SQL 與 Pandas：Pandas 操作可對應 SQL 的 where、group by、distinct、case when、join；可用 `pandas.read_sql` 直接載入查詢結果。強調面試普遍要求 SQL Hard 題，需練習 window function（`row_number`/`cume_dist` 類型）處理每組前 N 筆或依順序挑選資料。
- 系統設計練習：討論資料平台高階架構題（來源為網站行為與實體店面檔案），需描述資料流、儲存、模型串接，並分別滿足行銷主管（可用性與回溯）、資料主管（流程監控）、資安主管（敏感資料權限與合規）的需求。
