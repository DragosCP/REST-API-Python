# this file just contains the blocklist of the JWT tokens. It will be imported by the app and the logout resources so that tokens can be added to the blocklist when the user logs out.

# this python set is used for demonstration purposes, we usually use a DB or Redis (is a persistent non-relational in-memory db) to store our blocklist
# at the moment, if we restart the app, even if we logout, we can make a request by getting all the items with the old JWT.

BLOCKLIST = set()