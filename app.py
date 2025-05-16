from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import config
from routes import user_routes

app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI

mongo = PyMongo(app)
CORS(app)


@app.before_request
def check_mongo_connection():
    if app.mongo is None:
        print("MongoDB connection error!")
    else:
        print("The connection to MongoDB is working properly.")


app.mongo = mongo
app.register_blueprint(user_routes, url_prefix="/api/users")


@app.route("/routes")
def list_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])


if __name__ == "__main__":
    app.run(debug=True)
