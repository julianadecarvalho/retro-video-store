from flask import current_app
from app import db
from datetime import datetime


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    postal_code = db.Column(db.String)
    phone = db.Column(db.String)
    registered_at = db.Column(db.DateTime)
    videos_checked_out_count = db.Column(db.Integer)

    def resp_json(self):
        if self.registered_at:
            register = datetime.datetime(self.registered_at)
        else:
            register = None
        customer_info = {
            "id": self.customer_id,
            "name": self.name,
            "registered_at": self.registered_at,
            "postal_code": int(self.postal_code),
            "phone": self.phone,
            "videos_checked_out_count": 0
        }

        return customer_info 