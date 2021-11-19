# import dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from sqlalchemy.sql.expression import all_

# Database setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to tables
measurement = Base.classes.measurement
station = Base.classes.station


# Flask setup
app = Flask(__name__)

# Flask routes
# home page
@app.route("/")
def home():
    return(
        f"Welcome to Climate App<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# precipitation query page
@app.route("/api/v1.0/precipitation")
def precip():
# create session
    session = Session(engine)
    precip = session.query(measurement.date, measurement.prcp).all()
    session.close()
    all_precip = list(np.ravel(precip))
    return jsonify(all_precip)

# # station query page
# @app.route("/api/v1.0/stations")
# def stations():
#     return jsonify()

# # temperature query page
# @app.route("/api/v1.0/tobs")
# def tobs():
#     return jsonify()

####The hard part####

#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

if __name__ == "__main__":
    app.run(debug=True)    