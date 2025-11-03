#!/bin/bash

echo "======================================"
echo "  營養素補充最佳化工具"
echo "======================================"
echo ""

# 檢查 Python 是否安裝
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未安裝，請先安裝 Python 3"
    exit 1
fi

echo "✅ Python 已安裝"

# 檢查 Flask 是否安裝
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚙️  正在安裝 Flask..."
    pip install flask --break-system-packages
else
    echo "✅ Flask 已安裝"
fi

echo ""
echo "🚀 啟動伺服器..."
echo ""
echo "請在瀏覽器中開啟："
echo "👉 http://localhost:5000"
echo ""
echo "按 Ctrl+C 停止伺服器"
echo ""

python3 nutrition_optimizer.py
