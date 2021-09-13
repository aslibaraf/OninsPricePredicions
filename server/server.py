from flask import Flask, request, jsonify
import util

app = Flask(__name__)
@app.route('/marketlist', methods=['GET'])
def marketlist():
    response = jsonify({
        'locations': util.marketlist()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_modalprice', methods=['GET', 'POST'])
def predict_modalprice():
    market = request.form['market']
    min_price = float(request.form['min_price'])
    max_price = float(request.form['max_price'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(market,min_price,max_price)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()