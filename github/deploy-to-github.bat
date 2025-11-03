@echo off
echo ====================================
echo   營養素補充最佳化工具 - GitHub 上傳
echo ====================================
echo.

REM 檢查是否已經初始化 git
if not exist .git (
    echo 正在初始化 Git...
    git init
    git branch -M main
)

echo.
echo 請輸入你的 GitHub repository 網址
echo 例如: https://github.com/你的帳號/nutrition-optimizer.git
set /p REPO_URL="GitHub URL: "

echo.
echo 正在上傳檔案到 GitHub...
git add .
git commit -m "Update: %date% %time%"

REM 設定 remote（如果還沒設定）
git remote remove origin 2>nul
git remote add origin %REPO_URL%

git push -u origin main

echo.
echo ====================================
echo   上傳完成！
echo ====================================
echo.
echo 接下來請到 Render.com 部署你的應用程式
echo 詳細步驟請參考 DEPLOYMENT.md
echo.
pause
