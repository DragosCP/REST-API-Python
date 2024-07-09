# import uuid
# from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

# from db import items
from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", "items", description="Operations on items")

@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
        # try:
        #     return items[item_id]
        # except KeyError:
        #     abort(400, message="Item not found.")

    @jwt_required()
    def delete(self, item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")
            # only the user with user_ID == 1 can delete the items. 
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}
        # raise NotImplementedError("Deleting an item is not implemented.")

        # try:
        #     del items[item_id]
        #     return {"message": "Item deleted."}
        # except KeyError:
        #     abort(404, message="Item not found.")
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id) #we've deleted the _or_404
        # this is slightly wrong, as if we don't have the item, it will automatically create it for us, altough we wanted to update an existing item. So:
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        # raise NotImplementedError("Updating an item is not implemented.")

        db.session.add(item)
        db.session.commit()

        return item


        # item_data = request.get_json()
        # if "price" not in item_data or "name" not in item_data:
        #     abort(400, message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.")
        # try:
        #     item = items[item_id]
            #item being a dictionary, we can updated with the operator |=
            #it merges 2 dictionaries, the item dictionary goes first and any values that are in item_data are replacing the value of item.
        #     item |= item_data
        #     return item
        # except KeyError:
        #     abort(400, message="Item not found.")
    
@blp.route("/item")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all() #items.values() #{"items": list(items.values())}
    
    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item 
       
        # item_data = request.get_json()
        # if (
        #     "price" not in item_data
        #     or "store_id" not in item_data
        #     or "name" not in item_data
        # ):
        #     abort(400, message=f"Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload")
        # now that we have a db that will check for us things like if it's string, nullable, unique etc, we don't need the below checks and of course the "items"
        # for item in items.values():
        #     if (
        #         item_data["name"] == item["name"]
        #         and item_data["store_id"] == item["store_id"]
        #     ):
        #         abort(400, message=f"Item already exists.")
        
        # item_id = uuid.uuid4().hex
        # item = {**item_data, "id": item_id}
        # items[item_id] = item
        # return item

        