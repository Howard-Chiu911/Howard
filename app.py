from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)  # 這會允許所有的跨域請求

@app.route('/api/encrypt', methods=['GET'])
def encrypt_data():
    key = request.args.get('key')
    source = request.args.get('source')
    create_date = request.args.get('createDate')
    
    if not key or not source or not create_date:
        return jsonify({"error": "Missing parameters"}), 400
    
    try:
        # 確保使用半角逗號
        str_check = f"{key},{source},{create_date}"
        
        # 打印出 str_check 來檢查傳入參數
        print(f"str_check: {str_check}")
        
        # 使用 UTF-8 編碼進行 MD5 加密
        encrypted = hashlib.md5(str_check.encode('utf-8')).hexdigest().upper()
        
        # 返回加密結果
        return jsonify({"encrypted": encrypted})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
