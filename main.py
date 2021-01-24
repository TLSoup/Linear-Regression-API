from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class ListingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    sqft = db.Column(db.Integer, nullable=False)
    bdrms = db.Column(db.Float, nullable=False)
    pool = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Listing( cost = {cost}, sqft = {sqft}, bdrms = {bdrms}, pool = {pool})"


#Only run once with this, or it will create the db a second time and delete current db.
#db.create_all()

listing_put_args = reqparse.RequestParser()
listing_put_args.add_argument("cost", type=int, help="Cost of listing is required", required=True)
listing_put_args.add_argument("bdrms", type=float, help="Number of bedrooms", required=True)
listing_put_args.add_argument("sqft", type=int, help="Square footage", required=True)
listing_put_args.add_argument("pool", type=int, help="Number of pools- 0 for none", required=True)

listing_update_args = reqparse.RequestParser()
listing_update_args.add_argument("cost", type=int, help="Cost of listing is required")
listing_update_args.add_argument("bdrms", type=float, help="Number of bedrooms")
listing_update_args.add_argument("sqft", type=int, help="Square footage")
listing_update_args.add_argument("pool", type=int, help="Number of pools- 0 for none")

listing_delete_args = reqparse.RequestParser()
listing_delete_args.add_argument("cost")
listing_delete_args.add_argument("bdrms")
listing_delete_args.add_argument("sqft")
listing_delete_args.add_argument("pool")


resource_fields = {
    'id': fields.Integer,
    'cost': fields.Integer,
    'sqft': fields.Integer,
    'bdrms': fields.Integer,
    'pool': fields.Integer
}

class Listing(Resource):
    @marshal_with(resource_fields)
    def get(self, listing_id):
        result = ListingModel.query.filter_by(id= listing_id).first()
        if not result:
            abort(404, message=("Could not find listing with that id"))
        return result
    
    @marshal_with(resource_fields)
    def put(self, listing_id):
        args = listing_put_args.parse_args()
        result = ListingModel.query.filter_by(id= listing_id).first()
        if result:
            abort(409, message="Listing id is taken...")
        listing = ListingModel(id= listing_id, cost=args['cost'], sqft=args['sqft'], bdrms=args['bdrms'], pool=args['pool'])
        db.session.add(listing)
        db.session.commit()
        return listing, 201
    
    @marshal_with(resource_fields)
    def patch(self, listing_id):
        args = listing_update_args.parse_args()
        result = ListingModel.query.filter_by(id= listing_id).first()
        if not result:
            abort(404, message="Listing does not exist, cannot update")
        
        if args['cost']:
            result.cost = args['cost']
        if args ['bdrms']:
            result.bdrms = args['bdrms']
        if args ['sqft']:
            result.sqft = args['sqft']
        if args ['pool']:
            result.pool = args['pool']

        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def delete(self, listing_id):
        args = listing_delete_args.parse_args()
        result = ListingModel.query.filter_by(id= listing_id).first()
        if not result:
            abort(404, message=("Could not find listing with that id"))
        listing = ListingModel(id= listing_id, cost=args['cost'], sqft=args['sqft'], bdrms=args['bdrms'], pool=args['pool'])
        db.session.delete(listing)
        db.session.commit()
        return 204, "Listing has been deleted"

api.add_resource(Listing, "/listing/<int:listing_id>")

if __name__ == "__main__":
    app.run(debug=True)

