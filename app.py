from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException


app= Flask(__name__)

@app.route("/",methods=["Get","post"])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info("WE are testing logging module")
        logging.info("WE are starting logging file")
    return "Starting machine learning Project"


if __name__ == "__main__":
    app.run(debug=True)