from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import json

import linear_regression as regression

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listings.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

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

class ListingListResource(Resource):
    def get(self):
        listings = Listing.query.all()
        return listings_schema.dump(listings)

    def post(self):
        """
        TODO: validate that data is an array of objects by inspecting the output of the print statement below
        """
        data = request.json()
        print(data)
        new_listings = [Listing(x.cost, x.sqft, x.bdrms, x.pool) for x in data]
        
        # TODO: regression should return the values that are stated in the README
        return_data = regression(new_listings)
        print(return_data)
        # db.session.add(new_listing)
        # db.session.commit()
        # TODO: regresstion
        return listing_schema.jsonify(return_data)

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


api.add_resource(ListingListResource, '/listings')
api.add_resource(ListingResource, '/listings/<int:listing_id>')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)