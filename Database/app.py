# compose_flask/app.py
from flask import Flask, request
import json


from __init__ import create_app, db
from models import Cats


app = create_app()


@app.route('/test', methods=['GET'])
def fetch():
    cats = Cats.query.all()
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return 'print'


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    cat = Cats(name=name, price=price, breed=breed)
    db.session.add(cat)
    db.session.commit()
    return json.dumps("Added"), 200


@app.route('/remove/<cat_id>', methods=['Delete'])
def remove(cat_id):
    Cats.query.filter_by(id=cat_id).delete()
    db.session.commit()
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    cat_to_update = Cats.query.filter_by(id=cat_id).all()[0]
    cat_to_update.price = new_price
    db.session.commit()
    return json.dumps("Edited"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)