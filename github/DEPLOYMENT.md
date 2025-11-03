# 🌐 部署到網路上的完整教學

本文件會教你如何將營養素補充最佳化工具部署到網路上，讓任何人都能透過網址訪問。

## 📋 目錄

1. [方案比較](#方案比較)
2. [推薦方案：Render.com（免費）](#推薦方案rendercom免費)
3. [其他部署選項](#其他部署選項)
4. [進階：使用資料庫持久化儲存](#進階使用資料庫持久化儲存)

---

## 方案比較

| 平台 | 費用 | 難度 | 速度 | 推薦度 |
|------|------|------|------|--------|
| **Render.com** | 免費 | ⭐ 簡單 | 中等 | ⭐⭐⭐⭐⭐ |
| **Railway.app** | 免費額度 | ⭐⭐ 簡單 | 快 | ⭐⭐⭐⭐ |
| **PythonAnywhere** | 免費 | ⭐⭐ 中等 | 中等 | ⭐⭐⭐ |
| **Heroku** | $5/月起 | ⭐⭐ 中等 | 快 | ⭐⭐⭐ |
| **VPS (DigitalOcean等)** | $6/月起 | ⭐⭐⭐⭐ 困難 | 很快 | ⭐⭐ |

---

## 推薦方案：Render.com（免費）

### 🎯 為什麼選 Render？

- ✅ **完全免費**（有免費方案）
- ✅ **超級簡單**（5分鐘部署完成）
- ✅ **自動 HTTPS**（網站有安全鎖）
- ✅ **自動部署**（更新 GitHub 就自動更新網站）
- ⚠️ **限制**：15分鐘沒人用會休眠，下次訪問需等待10-20秒啟動

### 📝 部署步驟

#### 步驟 1：註冊 GitHub 帳號（如果還沒有）

1. 前往 https://github.com
2. 點擊 **Sign up** 註冊
3. 完成註冊並登入

#### 步驟 2：上傳程式碼到 GitHub

1. 在 GitHub 上點擊右上角 `+` → `New repository`
2. 填寫：
   - Repository name: `nutrition-optimizer`（或你喜歡的名稱）
   - 選擇 **Public**（公開）
   - 點擊 **Create repository**

3. 在你的電腦上：
   ```bash
   cd nutrition-optimizer  # 進入專案資料夾
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/你的帳號/nutrition-optimizer.git
   git push -u origin main
   ```

   **如果你不熟悉 Git，可以用 GitHub 網頁版上傳：**
   - 點擊 **uploading an existing file**
   - 把所有檔案拖曳上去
   - 點擊 **Commit changes**

#### 步驟 3：註冊 Render.com

1. 前往 https://render.com
2. 點擊 **Get Started**
3. 選擇 **Sign in with GitHub**（用 GitHub 帳號登入）
4. 授權 Render 存取你的 GitHub

#### 步驟 4：建立 Web Service

1. 登入 Render 後，點擊 **New +** → **Web Service**
2. 選擇你剛才上傳的 `nutrition-optimizer` repository
3. 填寫設定：
   - **Name**: `nutrition-optimizer`（會變成網址的一部分）
   - **Region**: 選擇 `Singapore`（最接近台灣）
   - **Branch**: `main`
   - **Root Directory**: 留空
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn nutrition_optimizer:app`
   - **Instance Type**: 選擇 **Free**

4. 點擊 **Create Web Service**

#### 步驟 5：等待部署完成

- Render 會自動：
  1. 下載你的程式碼
  2. 安裝 Flask 和相關套件
  3. 啟動伺服器
  
- 需要約 2-3 分鐘
- 完成後會顯示綠色的 **Live** 狀態

#### 步驟 6：訪問你的網站！

- 你的網址會是：`https://nutrition-optimizer.onrender.com`
- 點擊網址就能訪問！
- 🎉 分享這個網址給朋友就能用了！

---

## 🔄 如何更新網站

當你修改程式碼後：

**方法 1：透過 GitHub（推薦）**
```bash
git add .
git commit -m "更新功能"
git push
```
Render 會自動偵測更新並重新部署！

**方法 2：手動重新部署**
- 進入 Render Dashboard
- 點擊你的服務
- 點擊右上角 **Manual Deploy** → **Deploy latest commit**

---

## 其他部署選項

### 選項 2：Railway.app

**優點：**
- 比 Render 更快
- 免費額度：每月 500 小時 + $5 credit
- 不會休眠

**步驟：**
1. 前往 https://railway.app
2. 用 GitHub 登入
3. **New Project** → **Deploy from GitHub repo**
4. 選擇你的 repository
5. Railway 會自動偵測 Python 專案並部署
6. 在 **Settings** → **Networking** 產生網域

### 選項 3：PythonAnywhere

**適合：** 想要更穩定的免費方案

**步驟：**
1. 註冊 https://www.pythonanywhere.com
2. 選擇 **Beginner** 帳號（免費）
3. 前往 **Web** 分頁
4. **Add a new web app**
5. 選擇 **Flask**
6. 上傳你的程式碼
7. 設定 WSGI configuration file

**詳細教學：** https://help.pythonanywhere.com/pages/Flask/

### 選項 4：Heroku（需付費）

**費用：** $5-7/月

**優點：**
- 效能穩定
- 不會休眠
- 支援資料庫

**步驟：**
1. 註冊 https://heroku.com
2. 安裝 Heroku CLI
3. 在專案資料夾執行：
   ```bash
   heroku login
   heroku create nutrition-optimizer
   git push heroku main
   ```

### 選項 5：VPS 主機（進階）

**平台：** DigitalOcean、Linode、AWS EC2、GCP

**費用：** $5-10/月起

**需要技能：**
- Linux 指令
- Nginx 設定
- 防火牆設定
- SSL 憑證設定

**不推薦新手，除非你想學習伺服器管理**

---

## 進階：使用資料庫持久化儲存

目前程式的資料儲存在記憶體中，**重啟後資料會消失**。

如果想要永久儲存資料，可以使用資料庫：

### 選擇 1：SQLite（簡單）

**優點：** 不需要額外服務，檔案式資料庫
**缺點：** 雲端平台重啟後可能丟失

修改程式碼使用 SQLite：
```python
import sqlite3
import json

# 初始化資料庫
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS requirements
                 (data TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (data TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS solutions
                 (data TEXT)''')
    conn.commit()
    conn.close()

# 儲存資料
def save_requirements(data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM requirements")
    c.execute("INSERT INTO requirements VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()
```

### 選擇 2：PostgreSQL（推薦長期使用）

**免費資料庫服務：**
- [Supabase](https://supabase.com) - 免費 500MB
- [ElephantSQL](https://www.elephantsql.com) - 免費 20MB
- [Render PostgreSQL](https://render.com/docs/databases) - 免費 90天

**修改程式碼連接 PostgreSQL：**
```bash
pip install psycopg2-binary
```

```python
import psycopg2
import os

DATABASE_URL = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
```

### 選擇 3：JSON 檔案（最簡單）

在程式結束時將資料寫入 JSON 檔案：

```python
import json

def save_to_file():
    data = {
        'requirements': nutrition_requirements,
        'products': products,
        'solutions': solutions
    }
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_file():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'requirements': {}, 'products': {}, 'solutions': []}
```

**注意：** 多用戶同時使用可能會有資料衝突問題

---

## 🔒 安全性建議

如果你的網站會有多人使用，建議：

1. **加入使用者登入系統**
   - 使用 Flask-Login
   - 每個使用者有自己的資料

2. **加入 CSRF 保護**
   ```bash
   pip install flask-wtf
   ```

3. **限制 API 請求頻率**
   - 防止惡意使用
   - 使用 Flask-Limiter

4. **環境變數管理**
   - 敏感資訊（如資料庫密碼）不要寫在程式碼裡
   - 使用 `.env` 檔案

---

## ❓ 常見問題

### Q1：部署後網站打不開？

**檢查：**
1. Render 服務狀態是否為 **Live**（綠色）
2. Logs 中是否有錯誤訊息
3. 檢查 `requirements.txt` 是否正確

### Q2：為什麼第一次打開很慢？

免費版會休眠，第一次訪問需要 10-20 秒喚醒。可以：
- 升級到付費方案（$7/月）
- 使用 Railway（不會休眠）
- 使用 uptimerobot.com 定期 ping 你的網站（保持喚醒）

### Q3：資料會不會被別人看到？

目前所有人共用同一份資料。如果想要：
- **私人使用**：不要分享網址，或加入密碼保護
- **多人各自資料**：需要加入使用者登入系統

### Q4：如何加入自訂網域名稱？

在 Render：
1. 購買網域（GoDaddy、Namecheap 等）
2. 在 Render Dashboard → Settings → Custom Domain
3. 新增你的網域並設定 DNS

### Q5：可以改成中文網址嗎？

可以，但需要：
1. 購買中文網域
2. 設定 DNS 指向 Render 提供的網址

---

## 🎯 建議的部署流程

**個人使用 / 小範圍分享：**
1. ✅ Render.com 免費版
2. 不需要資料庫
3. 定期手動備份資料

**想長期使用 / 多人分享：**
1. ✅ Railway.app 或 Render 付費版
2. ✅ 使用 PostgreSQL 資料庫
3. ✅ 加入使用者登入系統

**學習用途：**
1. ✅ 先用 Render 免費版體驗
2. ✅ 學習 Git 和部署流程
3. ✅ 之後再升級功能

---

## 📚 延伸學習資源

- [Flask 部署官方文件](https://flask.palletsprojects.com/en/3.0.x/deploying/)
- [Render Python 教學](https://render.com/docs/deploy-flask)
- [Railway 文件](https://docs.railway.app/)
- [免費 PostgreSQL 資料庫比較](https://github.com/ripienaar/free-for-dev#dbaas)

---

## 💬 需要幫助？

如果部署遇到問題：
1. 查看 Render Dashboard 的 Logs
2. 確認 GitHub repository 中的檔案完整
3. 檢查 `requirements.txt` 和 `Procfile` 是否正確

祝部署順利！🚀
