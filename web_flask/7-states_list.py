#!/usr/bin/python3
""" flask app """
from flask import Flask, render_template, request, g
import mysql.connector

app = Flask(__name__)


def connect_db():
    """ connect database """
    return mysql.connector.connect(
        host='localhost',
        user='zakaria',
        password='1L0v3T0C0d3!',
        database='hbnb_dev_db'
    )


@app.teardown_appcontext
def teardown(exception):
    """Close the database connection"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.cursor().close()


@app.route('/states_list', strict_slashes=False)
def show_data():
    """ show data """
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    states = cursor.fetchall()
    cursor.close()
    sorted_states = sorted(states, key=lambda state: state[3])
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
