from flask import Flask, request, jsonify

# 初始化Flask应用
app = Flask(__name__)

# 从问题1的回归结果中获取参数（硬编码）
ALPHA = 93.5005
TAU = -5.0001
BETA = 1.4999

# 定义预测端点
@app.route('/predict', methods=['GET'])
def predict():
    try:
        # 从URL参数中获取W和X的值，并转换为正确类型
        W = int(request.args.get('W', 0))  # 默认值0
        X = float(request.args.get('X', 0)) # 默认值0.0
    except ValueError:
        # 处理非法参数（例如非数字输入）
        return jsonify({'error': 'Invalid parameter type. W must be 0/1, X must be a number.'}), 400

    # 计算预测值（公式：Y = α + τ*W + β*X）
    y_pred = ALPHA + TAU * W + BETA * X

    # 返回JSON格式结果，保留两位小数
    return jsonify({
        'predicted_engagement': round(y_pred, 2)
    })

# 主程序入口
if __name__ == '__main__':
    # 启动Flask服务，监听所有IP地址的5000端口
    app.run(host='0.0.0.0', port=5000)
