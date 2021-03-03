from flask import Flask, Response, request, jsonify
import json

app = Flask(__name__)

NAMES = {
    "001": {"name": "matt", "age": 30, "city": "San Diego"},
    "002": {"name": "sam", "age": 28, "city": "San Diego"},
    "003": {"name": "gina", "age": 32, "city": "Portland"},
    "004": {"name": "lara", "age": 40, "city": "San Francisco"}}

# handling data entry for POST and PUT requests


def process_entry(id, user_input):
    if "name" not in user_input or "age" not in user_input or "city" not in user_input:
        return Response("you need to include name, age and city", status=400, mimetype='text/xml')

    elif type(user_input["name"]) is not str or len(user_input["name"]) > 100:
        return Response("name must be a string with length no longer than 100 characters", status=400, mimetype='text/xml')

    elif type(user_input["city"]) is not str or len(user_input["city"]) > 100:
        return Response("city must be a string with length no longer than 100 characters", status=400, mimetype='text/xml')

    elif type(user_input["age"]) is not int or user_input["age"] < 0 or user_input["age"] >= 122:
        return Response("age must be an integer between 0 and 122", status=400, mimetype='text/xml')

    else:
        NAMES[id] = user_input
        return Response(f"inserted {id}", status=200, mimetype='text/xml')


# setting up the route to display all names in the dictionary
@app.route('/all-names/', methods=['GET'])
def get_all_names():
    return jsonify(NAMES)


# description of the query formation; declaring all of the methods
@app.route('/name/<string:id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_name_data(id):

    if request.method == 'GET':
        if id in NAMES:  # if the id exists in the dictionary  return it as json
            return jsonify(NAMES[id])
        else:
            # adding status to the response to help manage debugging
            return Response(f"{id} is not part of our data set", status=400, mimetype='text/xml')

    if request.method == 'POST':
        # return the dictionary related to the specified id
        user_input = request.get_json()
        return process_entry(id, user_input)

    if request.method == 'DELETE':
        if id in NAMES:
            del NAMES[id]
            return Response(f"Deleted {id}", status=400, mimetype='text/xml')
        else:
            return Response(f"{id} does not exist")

    if request.method == 'PUT':
        if id in NAMES:
            user_input = request.get_json()  # this request.json comes from the body
            return process_entry(id, user_input)
        else:
            return Response(f"{id} does not exist", status=400)


if __name__ == "__main__":
    app.run(debug=True)
