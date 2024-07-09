
# VS CODE shorcuts:
#   ALT+Z = Wrap Text
#   CTRL + J = Open Terminal
#   CTRL + / = Comment

# Here is what our REST API is going to do: it will receive requests from a client such as a mobile application/mobile app and we will respond with some data
#
# !!!!!!!!!! The main benefit of having a REST API is that multiple applications can make requests to the same API and thereby share resources such as a DataBase. !!!!!!!
#
# So when a client makes a request such as he wants to create a store, our API will create a store and put it in the DB and then multiple clients will be able to get information about that same store.

# Create stores, each with a "name" and a list of stocked "items"
# Create an item within a store, each with a "name" and a "price"
# Retrieve its "name", retrieve an individual store and all its items
# Given a store "name", retrieve only a list of item within it.


# 1.Create stores
# Request: POST /store {"name": "My Store"}
# Response: {"name": "My store", "items": [1]}

# 2.Create items
# Request: POST /store/My Store/item {"name": "Chair", "price": 175.50}
# Response: {"name": "Chair", "price": 175.50}

# 3.Retrieve all stores and their items
# Request: GET /store
# Response: {"stores":[{"name": "My Store", "items": [{"name": "Chair", "price": 165.50}]}]}

# 4. Get a particular store
# Request: GET /store/My Store
# Response: {"name": "My Store", "items": [{"name": "Chair", "price": 165.50}]}

# 5. Get only items in a store
# Request: GET /store/My Store/item
# Response: [{"name": "Chair", "price": 165.50}]