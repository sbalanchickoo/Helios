from masterdataapi import app
from flask import make_response, jsonify, request
from views.data_retrieve import *


@app.route("/masterdata/api/v1/states", methods=['GET'])
def return_states():
    states_result = get_states()
    response = jsonify(states = states_result)
    return response




