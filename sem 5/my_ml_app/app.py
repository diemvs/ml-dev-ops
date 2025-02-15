from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    try:
        data = request.get_json()

        if 'numbers' not in data or not isinstance(data['numbers'], list):
            return jsonify({"error": "Invalid input, expected JSON with 'numbers' list"}), 400

        numbers = np.array(data['numbers'])
        total = np.sum(numbers)

        return jsonify({"sum": float(total)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)