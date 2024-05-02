from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb+srv://jimmyjimmy0226:XCvJqawUzPr2aaCd@ctf.bkczoed.mongodb.net/"
client = MongoClient(mongo_uri)
db = client.get_database('ctf')
collection = db.get_collection('ctf')

@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {'_id': 0, 'user_id': 1}))
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
