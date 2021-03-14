import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os
import psycopg2

from flask import Flask, jsonify, render_template

from config import password

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (46.9540700, 142.7360300)

@app.route('/lapseScrape')
def lapseScrape(startDate, endDate):
    strSQL = "SELECT "


if __name__ == '__main__':
    app.run(debug=True)
# #################################################
# # Database Setup
# #################################################
# create connection to ETL_project_DB in postgres
engine = create_engine('postgresql://postgres:'+ password + '@localhost:5432/AirQuality_DB')
connection = engine.connect()

# Check for table names
engine.table_names()

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table


# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)


# #################################################
# # Flask Routes
# #################################################

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route("/about")
# def about():
#     return render_template('html/info.html')

# @app.route("/sources")
# def sources():
#     return render_template('html/resources.html')

# @app.route("/members")
# def members():
#     return render_template('html/members.html')

# @app.route("/current")
# def current():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # # Query 
#     # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # # Create a dictionary from the row data and append to a list of all_passengers
#     # all_passengers = []
#     # for name, age, sex in results:
#     #     passenger_dict = {}
#     #     passenger_dict["name"] = name
#     #     passenger_dict["age"] = age
#     #     passenger_dict["sex"] = sex
#     #     all_passengers.append(passenger_dict)

#     #return jsonify(all_passengers)

# @app.route("/historical")
# def historical():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # # Query 
#     # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # # Create a dictionary from the row data and append to a list of all_passengers
#     # all_passengers = []
#     # for name, age, sex in results:
#     #     passenger_dict = {}
#     #     passenger_dict["name"] = name
#     #     passenger_dict["age"] = age
#     #     passenger_dict["sex"] = sex
#     #     all_passengers.append(passenger_dict)

#     #return jsonify(all_passengers)

# @app.route("/timelapse")
# def timelapse():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # # Query 
#     # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # # Create a dictionary from the row data and append to a list of all_passengers
#     # all_passengers = []
#     # for name, age, sex in results:
#     #     passenger_dict = {}
#     #     passenger_dict["name"] = name
#     #     passenger_dict["age"] = age
#     #     passenger_dict["sex"] = sex
#     #     all_passengers.append(passenger_dict)

#     #return jsonify(all_passengers)

# if __name__ == '__main__':
#     app.run(debug=True)