# Tibame 20251206 pyetl afternoon

- 連線 MySQL：安裝 `pymysql`（負責連線）與 `SQLAlchemy`（讓 pandas 取得 schema/型別）。MySQL 連線 URI 範例 `mysql+pymysql://user:password@host:3306/dbname`，可於 query string 加 `autocommit=true`。
- 建置練習環境：以 Workbench 建 `testDB` 與 `staff` 表；確認帳密/連得進去再寫程式。Workbench 只支援 MySQL，DBeaver 可跨資料庫。
- 基本 cursor 操作：`cursor.execute(sql)` 執行單筆；`executemany(sql, data)` 批次；查詢用 `fetchall/fetchone`，資料被 fetch 後不可重取。結束時 `cursor.close()`、`connection.close()`。
- 交易與例外處理：會動到資料庫或可能中斷交易的操作需 `try/except`，處理已知錯誤（如 PK 重複的 IntegrityError），未知錯誤記錄後仍要在 `finally` 確保 `commit` 或 `rollback` 並關閉連線。密碼錯誤等可用 if/else 先行檢查。
- pandas 與資料庫：`pd.read_sql(query, engine)` 讀表/查詢，`DataFrame.to_sql(..., if_exists='append|replace|fail')` 寫回；`replace` 會刪表重建再寫入，實際有隱含 commit。auto-commit 常直接開啟以減少手動 commit；避免 PK 重複可先調整主鍵值。
- Debug 心法：操作流程長時，逐步檢視中間 DataFrame、用 filter 聚焦少量資料，必要時重置表到初始狀態再重跑。
- ORM 簡介：SQLAlchemy ORM 透過 `create_engine` + model class 定義欄位型別/主鍵/nullable，session.query 取得資料；對 SQL 熟練者可直接寫 SQL，ORM 主要幫助不熟 SQL 的人。
- 工具與生態：pandas 仍主流；提到 polars 介面相似但速度更快。MySQL 常有鎖/錯誤議題，業界常用 PostgreSQL；PostgreSQL 支援 JSON 欄位，常可取代 MongoDB 使用情境。
