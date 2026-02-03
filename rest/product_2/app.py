from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

products = []

@app.route('/register/product', methods=['POST'])
def register_product():
    data = request.get_json()

    required_fields = [
        "cat_id",
        "sub_id",
        "product_name",
        "price",
        "gst",
        "offer",
        "image"
    ]

    missing = [field for field in required_fields if field not in data or data[field] in (None, "")]
    if missing:
        return jsonify({
            "status": "error",
            "message": f"reason: missing fields {''.join(missing)}"
        }), 400

    with open(data["image"], "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    print(encoded_string)

    data["image"] = f"data:image/jpg;base64,{encoded_string}"

    try:
        base64.b64decode(encoded_string)
    except Exception:
        return jsonify({
            "status": "error",
            "message": "invalid base64 image"
        }), 400
    
    products.append(data)
    return jsonify({
        "status": "success",
        "message": "product registered",
        "product": data
    }), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(port=3000, debug=True)
