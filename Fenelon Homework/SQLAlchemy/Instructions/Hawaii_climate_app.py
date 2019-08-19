#Import Dependices & Libraries
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


#################################################
# Flask Setup
#################################################
hawaii_climate_app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Hawaii Climate Station API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
 
 #Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
 #Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)
    prcp_results = session.query(Measurement.date, Measurement.prcp).group_by(Measurement.date).all()
    session.close()

    precipitation = []
    for date, prcp in prcp_results:
        Hawaii_prcp = {}
        Hawaii_prcp["date"] = date
        Hawaii_prcp["prcp"] = prcp
        precipitation.append(Hawaii_prcp)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_results = session.query(Station.stations).all()
    session.close()
    
    return jsonify(station_results)

  # query for the dates and temperature observations from a year from the last data point.
  # Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= dt.datetime(2016, 8, 23)).\
        filter(Measurement.date <= dt.datetime(2017, 8, 23)).\
        order_by(Measurement.date.desc()).all()

    session.close()

    tempature = []
    for temp in tobs_results:
        passenger_dict = {}
        YGO_temp["temp"] = temp
        tempature.append(YGO_temp)

    return jsonify(YGO_temp)


  # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start():
    session = Session(engine)




@app.route("/api/v1.0/<start>/<end>")
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
def start_end():
    session = Session(engine)



    return jsonify(all_passengers)

if __name__ == '__main__':
    hawaii_climate_app.run(debug=True)