# 🚀 5分鐘快速部署指南

想要把這個工具放到網路上讓別人用？跟著這個簡單的步驟就可以了！

## 📋 你需要的東西

1. ✅ GitHub 帳號（免費）
2. ✅ Render.com 帳號（免費）
3. ✅ 這個專案的檔案

**總時間：約 5-10 分鐘**

---

## 🎯 步驟 1：上傳到 GitHub（2分鐘）

### 方法 A：使用網頁版（最簡單）

1. **註冊/登入 GitHub**
   - 前往 https://github.com
   - 如果沒帳號，點擊 Sign up 註冊

2. **建立新的 Repository**
   - 點擊右上角 `+` → `New repository`
   - Repository name: `nutrition-optimizer`
   - 選擇 **Public**（公開）
   - ✅ 勾選 **Add a README file**
   - 點擊 **Create repository**

3. **上傳檔案**
   - 在 repository 頁面，點擊 **Add file** → **Upload files**
   - 把以下檔案全部拖進去：
     ```
     nutrition_optimizer.py
     requirements.txt
     Procfile
     templates/（整個資料夾）
     static/（整個資料夾）
     README.md
     .gitignore
     ```
   - 在下方輸入 "Initial commit"
   - 點擊 **Commit changes**

✅ **完成！你的程式碼已經在 GitHub 上了**

### 方法 B：使用指令（如果你會用 Git）

```bash
cd nutrition-optimizer
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的帳號/nutrition-optimizer.git
git push -u origin main
```

或直接執行：
- Windows: 雙擊 `deploy-to-github.bat`
- Mac/Linux: `bash deploy-to-github.sh`

---

## 🌐 步驟 2：部署到 Render（3分鐘）

1. **註冊/登入 Render**
   - 前往 https://render.com
   - 點擊 **Get Started**
   - 選擇 **Sign in with GitHub**（用你的 GitHub 帳號登入）
   - 授權 Render 存取你的 GitHub

2. **建立 Web Service**
   - 在 Render Dashboard，點擊 **New +** → **Web Service**
   - 找到並點擊 `nutrition-optimizer` repository
   - 如果沒看到，點擊 **Configure account** 授權存取

3. **設定服務**
   填寫以下資訊：
   
   | 欄位 | 填入內容 |
   |------|----------|
   | **Name** | `nutrition-optimizer` |
   | **Region** | Singapore（最接近台灣） |
   | **Branch** | main |
   | **Runtime** | Python 3 |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `gunicorn nutrition_optimizer:app` |
   | **Instance Type** | **Free** ⭐ |

4. **點擊 Create Web Service**

5. **等待部署**
   - Render 會開始建置（約 2-3 分鐘）
   - 看到綠色的 **Live** 就完成了！

6. **取得你的網址**
   - 網址會是：`https://nutrition-optimizer.onrender.com`
   - 或類似的名稱（根據你取的名字）

---

## 🎉 完成！

你的網站已經上線了！

- 🔗 **分享網址**：把網址傳給朋友就能用
- 📱 **手機也能用**：在任何裝置都能開啟
- 🔒 **有 HTTPS**：網站是安全的

---

## ⚠️ 免費版限制

Render 免費版的限制：
- ⏰ **15分鐘沒人用會休眠**
  - 下次訪問需要等 10-20 秒喚醒
  - 解決方法：升級到付費版（$7/月）或使用 uptimerobot.com 定期 ping
  
- 💾 **資料會在重啟後消失**
  - 目前資料儲存在記憶體中
  - 想要永久儲存？看 DEPLOYMENT.md 的資料庫教學

---

## 🔄 如何更新網站

當你修改程式碼後：

### 方法 1：透過 GitHub 網頁版
1. 到你的 GitHub repository
2. 點擊要修改的檔案
3. 點擊鉛筆圖示編輯
4. 編輯完點擊 **Commit changes**
5. Render 會自動偵測並重新部署！

### 方法 2：上傳新檔案
1. 到你的 GitHub repository  
2. 點擊 **Add file** → **Upload files**
3. 上傳修改過的檔案
4. Commit changes
5. Render 會自動更新！

### 方法 3：使用 Git 指令
```bash
git add .
git commit -m "更新功能"
git push
```

---

## 🆘 遇到問題？

### 問題 1：網站打不開

**檢查：**
1. Render Dashboard 的服務是否顯示綠色 **Live**
2. 點擊 **Logs** 查看錯誤訊息
3. 確認 `requirements.txt` 和 `Procfile` 在 GitHub 上

### 問題 2：部署失敗

**常見原因：**
- 檔案沒有完整上傳到 GitHub
- `requirements.txt` 內容錯誤
- Python 版本不符

**解決方法：**
- 檢查 Render 的 **Logs** 看錯誤訊息
- 確認所有檔案都在 GitHub 上
- 在 Render 設定中確認 Python 版本

### 問題 3：為什麼第一次開啟很慢？

這是正常的！免費版會休眠，第一次訪問需要 10-20 秒喚醒。

**解決方法：**
1. 等待喚醒（最簡單）
2. 升級到付費版（$7/月，不休眠）
3. 使用其他平台（Railway.app 免費版不休眠）

### 問題 4：資料不見了！

Render 重啟後記憶體會清空。

**解決方法：**
- 參考 DEPLOYMENT.md 設定資料庫
- 或手動匯出/匯入資料

---

## 💡 進階功能

完成基本部署後，你可以：

1. **加入資料庫**（永久儲存資料）
   - 參考 DEPLOYMENT.md
   - 推薦使用 Supabase（免費）

2. **自訂網域**
   - 購買網域（GoDaddy、Namecheap）
   - 在 Render 設定 Custom Domain

3. **加入使用者登入**
   - 使用 Flask-Login
   - 每個人有自己的資料

4. **提升效能**
   - 升級到付費方案
   - 使用 CDN 加速

詳細教學都在 **DEPLOYMENT.md** 裡！

---

## 🎓 其他部署選項

不想用 Render？還有這些選擇：

### Railway.app
- ✅ 更快，不會休眠
- ✅ 免費額度更多
- 📝 教學：DEPLOYMENT.md

### PythonAnywhere
- ✅ 專為 Python 設計
- ✅ 免費方案穩定
- 📝 教學：DEPLOYMENT.md

### Heroku
- 💰 需付費（$5/月）
- ✅ 穩定可靠
- 📝 教學：DEPLOYMENT.md

---

## 📚 下一步

- ✅ 部署成功 → 分享給朋友用
- ✅ 想要更穩定 → 看 DEPLOYMENT.md 設定資料庫
- ✅ 想要學更多 → 看 DEPLOYMENT.md 的進階功能

有問題隨時查看 **DEPLOYMENT.md** 完整教學！

祝你部署順利！🚀
