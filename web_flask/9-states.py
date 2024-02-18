from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_cities(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('state.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)