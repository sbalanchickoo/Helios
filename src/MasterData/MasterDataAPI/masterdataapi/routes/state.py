from flask import make_response, jsonify, request, url_for, Blueprint
from views.data_retrieve import get_state_by_abbrev, get_states

state_route = Blueprint('state', __name__)

def make_public_state(state):
    new_state = {}
    for field in state:
        if field == 'id':
            new_state['uri'] = url_for('state.return_state_by_abbrev', abbrev=state['abbrev'], _external=True)
        else:
            new_state[field] = state[field]
    return new_state


@state_route.route("/masterdata/api/v1/states", methods=['GET'])
def return_states():
    states = get_states()
    response = [make_public_state(i.serialize) for i in states]
    return jsonify({'states': response})


@state_route.route("/masterdata/api/v1/state/abbrev/<string:abbrev>", methods=['GET'])
def return_state_by_abbrev(abbrev):
    state = get_state_by_abbrev(abbrev)
    response = [make_public_state(i.serialize) for i in state]
    if len(response) == 0:
        return make_response(jsonify({'error': 'Not found'}), 404)
    else:
        return jsonify({'state': response})



