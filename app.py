import sqlalchemy
from flask import Flask, jsonify, request

import helpers
from DB.Models.User import User
from config import app, db


@app.route("/api/contacts/<CONTACT_ID>", methods=["PUT"])
def put_user(CONTACT_ID):
    user = User.query.filter_by(id=int(CONTACT_ID)).update(request.json)
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


@app.route("/api/contacts", methods=["POST"])
def create_user():
    first_name = request.json.get("first_name")
    email = request.json.get("email")
    if not helpers.is_required_field(first_name):
        return jsonify({"ERROR": "first_name field is required"})
    if not helpers.is_required_field(email):
        return jsonify({"ERROR": "email field is required"})
    last_name = request.json.get("last_name")
    phone = request.json.get("phone")
    country = request.json.get("country")
    city = request.json.get("city")
    address = request.json.get("address")
    user = User(email=email, first_name=first_name, last_name=last_name, phone=phone, country=country, city=city,
                address=address)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"SUCCESS": f"User: {user} is created"})
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        user = User.query.filter_by(email=email).first()
        print(user)
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
    app.run(debug=True)
