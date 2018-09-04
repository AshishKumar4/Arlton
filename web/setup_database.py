import couchdb
from werkzeug.security import generate_password_hash, check_password_hash

db = couchdb.Server("http://localhost:5984/")
d = db.create("users")
d['admin'] = {"password" : generate_password_hash("admin"), "type":"admin"}

d = db.create('vehicles')
d['12345'] = {'milage':20, 'fuel':45, 'total_distance':12350, 'vnum':12345, 'total_tires':4, 'tires':{'1':120, '2':0213, '3':4230, '4':4650}}