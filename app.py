from flask import Flask, jsonify
from fileData import data

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Please navigate to '/get_data'"

@app.route('/get_data', methods=['GET'])
def get_data():
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug=True)
