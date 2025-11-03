from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# 儲存資料（實際應用可以改用資料庫）
nutrition_requirements = {}
products = {}
solutions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/requirements', methods=['GET', 'POST'])
def manage_requirements():
    global nutrition_requirements
    
    if request.method == 'POST':
        nutrition_requirements = request.json
        return jsonify({'status': 'success', 'data': nutrition_requirements})
    
    return jsonify(nutrition_requirements)

@app.route('/api/products', methods=['GET', 'POST'])
def manage_products():
    global products
    
    if request.method == 'POST':
        data = request.json
        product_id = data['id']
        products[product_id] = data
        return jsonify({'status': 'success', 'data': data})
    
    return jsonify(list(products.values()))

@app.route('/api/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    
    if product_id in products:
        del products[product_id]
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error', 'message': 'Product not found'}), 404

@app.route('/api/analyze', methods=['POST'])
def analyze_combination():
    data = request.json
    selected_products = data.get('products', [])
    
    if not nutrition_requirements:
        return jsonify({'error': '請先設定營養素需求'}), 400
    
    # 計算總營養素含量（每日）
    total_nutrients = {}
    daily_cost = 0
    product_details = []
    
    for item in selected_products:
        product_id = item.get('productId') if isinstance(item, dict) else item
        daily_serving = item.get('dailyServing', 1) if isinstance(item, dict) else 1
        
        if product_id in products:
            product = products[product_id]
            
            # 計算每日成本
            product_daily_cost = product['pricePerServing'] * daily_serving
            daily_cost += product_daily_cost
            
            # 計算可吃天數
            days_supply = int(product['totalServings'] / daily_serving) if daily_serving > 0 else 0
            
            product_details.append({
                'name': product['name'],
                'pricePerServing': round(product['pricePerServing'], 2),
                'dailyCost': round(product_daily_cost, 2),
                'dailyServing': daily_serving,
                'daysSupply': days_supply
            })
            
            # 計算每日營養素總量
            for nutrient, amount in product['nutrients'].items():
                daily_amount = amount * daily_serving
                total_nutrients[nutrient] = total_nutrients.get(nutrient, 0) + daily_amount
    
    # 分析缺口和過量
    analysis = {
        'sufficient': {},
        'insufficient': {},
        'excessive': {}
    }
    
    for nutrient, requirement in nutrition_requirements.items():
        min_val = requirement['min']
        max_val = requirement['max']
        current = total_nutrients.get(nutrient, 0)
        
        if current < min_val:
            analysis['insufficient'][nutrient] = {
                'current': round(current, 2),
                'required': min_val,
                'gap': round(min_val - current, 2),
                'unit': requirement['unit']
            }
        elif current > max_val:
            analysis['excessive'][nutrient] = {
                'current': round(current, 2),
                'max': max_val,
                'excess': round(current - max_val, 2),
                'unit': requirement['unit']
            }
        else:
            analysis['sufficient'][nutrient] = {
                'current': round(current, 2),
                'min': min_val,
                'max': max_val,
                'unit': requirement['unit']
            }
    
    result = {
        'products': product_details,
        'daily_cost': round(daily_cost, 2),
        'total_nutrients': total_nutrients,
        'analysis': analysis,
        'completeness': len(analysis['sufficient']) / len(nutrition_requirements) * 100 if nutrition_requirements else 0
    }
    
    return jsonify(result)

@app.route('/api/solutions', methods=['GET', 'POST'])
def manage_solutions():
    global solutions
    
    if request.method == 'POST':
        data = request.json
        data['id'] = len(solutions) + 1
        data['created_at'] = datetime.now().isoformat()
        solutions.append(data)
        return jsonify({'status': 'success', 'data': data})
    
    return jsonify(solutions)

@app.route('/api/solutions/<int:solution_id>', methods=['DELETE'])
def delete_solution(solution_id):
    global solutions
    
    solutions = [s for s in solutions if s['id'] != solution_id]
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
