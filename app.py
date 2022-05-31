import jsonschema
import sqlalchemy
from flask import Flask, jsonify, request
from flask_expects_json import expects_json
from jsonschema import ValidationError
import socket

from DB.Models.User import User
from config import app, db
from validate_json import validate_create_user_json, validate_change_user_info


@app.route("/api/contacts/<CONTACT_ID>", methods=["PUT"])
@expects_json(validate_change_user_info)
def put_user(CONTACT_ID):
    user = User.query.filter_by(id=int(CONTACT_ID)).first()
    if user is None:
        return jsonify({"ERROR": f"User with id: {CONTACT_ID} is not exists"})
    User.query.filter_by(id=int(CONTACT_ID)).update(request.json)
    db.session.commit()
    return jsonify({"MESSAGE": f"User with id: {CONTACT_ID} is changed"})


@app.route("/api/contacts/<CONTACT_ID>", methods=["DELETE"])
def delete_user(CONTACT_ID):
    user = User.query.get(int(CONTACT_ID))
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"MESSAGE": f"User with id: {CONTACT_ID} is deleted"})
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        return jsonify({"ERROR": f"User with id: {CONTACT_ID} is not exists"})


@app.errorhandler(400)
def validation_error(error):
    return jsonify({"ERROR": f"ValidationError {error.description}"})


@app.route("/api/contacts", methods=["POST"])
@expects_json(validate_create_user_json)
def create_user():
    email = request.json.get("email")
    user = User(**request.json)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"SUCCESS": f"User: {user} is created"})
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        user = User.query.filter_by(email=email).first()
        return jsonify({"ERROR": f"User: {user} is not created, because user has already been created"})


@app.route('/api/contacts/<CONTACT_ID>', methods=["GET"])
def get_contact(CONTACT_ID):
    user = User.query.get(int(CONTACT_ID))
    if user is None:
        return jsonify({"ERROR": f"User with id: {CONTACT_ID} not found"})
    return jsonify(user.to_json())


@app.route('/api/contacts', methods=["GET"])
def get_contacts():
    users = User.query.all()
    results = []
    for user in users:
        results.append(user.to_json())
    return jsonify(results)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
