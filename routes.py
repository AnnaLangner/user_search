from flask import Blueprint, request, jsonify, current_app
from bson import ObjectId
from models import serialize_user

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/", methods=["GET"])
def get_users():
    users = current_app.mongo.db.users.find()
    return jsonify([serialize_user(user) for user in users]), 200


@user_routes.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data or bad JSON format"}), 400

    required_fields = ("first_name", "last_name", "email")
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Required fields are missing"}), 400

    new_user = {
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"]
    }

    try:
        result = current_app.mongo.db.users.insert_one(new_user)
        user = current_app.mongo.db.users.find_one({"_id": result.inserted_id})
        return jsonify(serialize_user(user)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_routes.route("/<id>", methods=["GET"])
def get_user(id):
    user = current_app.mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(serialize_user(user)), 200
    return jsonify({"error": "User not found"}), 404


@user_routes.route("/search", methods=["GET"])
def search_users():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    query = {}
    if first_name:
        query["first_name"] = {"$regex": first_name, "$options": "i"}
    if last_name:
        query["last_name"] = {"$regex": last_name, "$options": "i"}

    users = current_app.mongo.db.users.find(query)
    return jsonify([serialize_user(user) for user in users]), 200
