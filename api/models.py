from . import db

# @todo: create models for the database tables

class DseStockPrices(db.Model):
    __tablename__ = 'dse_stock_prices'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    change = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'price': self.price,
            'change': self.change
        }