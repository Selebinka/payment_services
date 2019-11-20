from main import db

class Payments(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3))
    amount = db.Column(db.Integer)
    send_time = db.Column(db.Integer)
    discription = db.Column(db.Text)
    shop_order_id = db.Column(db.Integer)

    def __repr__(self):
        return 'Payments {}'.format(self.discription)