from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listing.db'
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    sqft = db.Column(db.Integer, nullable=False)
    bdrms = db.Column(db.Float, nullable=False)
    pool = db.Column(db.Integer, nullable=False)

class ListingSchema(ma.Schema):
    class Meta:
        fields = ("id", "cost", "sqft", "bdrms", "pool")
        model = Listing

listing_schema = ListingSchema()
listings_schema = ListingSchema(many=True)

# Get and Post for all listings
class ListingListResource(Resource):
    def get(self):
        listings = Listing.query.all()
        return listings_schema.dump(listings)
    
    def post(self):
        new_listing = Listing(
            cost=request.json['cost'],
            sqft=request.json['sqft'],
            bdrms=request.json['bdrms'],
            pool=request.json['pool']
        )
        db.session.add(new_listing)
        db.session.commit()
        return listing_schema.dump(new_listing)

api.add_resource(ListingListResource, '/listings')

# Get, Patch & Delete by listing_id
class ListingResource(Resource):
    def get(self, listing_id):
        listing = Listing.query.get_or_404(listing_id)
        return listing_schema.dump(listing)
    
    def patch(self, listing_id):
        listing = Listing.query.get_or_404(listing_id)

        if 'cost' in request.json:
            listing.cost = request.json['cost']
        if 'sqft' in request.json:
            listing.sqft = request.json['sqft']
        if 'bdrms' in request.json:
            listing.bdrms = request.json['bdrms']
        if 'pool' in request.json:
            listing.pool = request.json['pool']

        db.session.commit()
        return listing_schema.dump(listing)

    def delete(self, listing_id):
        listing = Listing.query.get_or_404(listing_id)
        db.session.delete(listing)
        db.session.commit()
        return '', 204 

api.add_resource(ListingResource, '/listings/<int:listing_id>')


if __name__ == '__main__':
    app.run(debug=True)