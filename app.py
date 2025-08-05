from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load data
df_prices = pd.read_csv('C:/Users/Daniel.Temesgen/Desktop/10 Academy/wk10/BrentOilPrices.csv')
df_prices['Date'] = pd.to_datetime(df_prices['Date'], format='mixed')
df_events = pd.read_csv('C:/Users/Daniel.Temesgen/Desktop/10 Academy/wk10/oil_market_events.csv')
df_events['Start Date'] = pd.to_datetime(df_events['Start Date'])

# Simulated model output (replace with actual trace from Task 2)
model_output = {
    'change_points': [15, 28],
    'means': [0.0, 0.01, 0.0],
    'runtime': 60.5
}

@app.route('/api/prices', methods=['GET'])
def get_prices():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    data = df_prices.copy()
    if start_date and end_date:
        data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(df_events.to_dict(orient='records'))

@app.route('/api/model', methods=['GET'])
def get_model():
    return jsonify(model_output)

if __name__ == '__main__':
    app.run(debug=True, port=5000)