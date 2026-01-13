from flask import request, jsonify
from config import create_app, db
from models import Plant

app = create_app()

# --------------------
# GET all plants
# --------------------
@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200

# --------------------
# GET a single plant by id
# --------------------
@app.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({"error": "Plant not found"}), 404
    return jsonify(plant.to_dict()), 200

# --------------------
# PATCH update plant
# --------------------
@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    data = request.get_json()
    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]
    if "price" in data:
        plant.price = data["price"]

    db.session.commit()
    return jsonify(plant.to_dict()), 200

# --------------------
# DELETE plant
# --------------------
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    db.session.delete(plant)
    db.session.commit()
    return "", 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)
