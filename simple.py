from flask import Flask, Response, request, jsonify
import json

app = Flask(__name__)

# returns the square of int added


@app.route('/square/<int:num>', methods=['GET'])
def get_square_data(num):

    return jsonify({'square': num**2})


if __name__ == "__main__":
    app.run(debug=True)
