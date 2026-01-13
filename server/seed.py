from app import app
from models import Plant
from config import db

with app.app_context():
    Plant.query.delete()

    plants = [
        Plant(
            name="Aloe",
            image="./images/aloe.jpg",
            price=11.50,
            is_in_stock=True
        ),
        Plant(
            name="Fern",
            image="./images/fern.jpg",
            price=15.00,
            is_in_stock=True
        )
    ]

    db.session.add_all(plants)
    db.session.commit()
