from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb+srv://jimmyjimmy0226:XCvJqawUzPr2aaCd@ctf.bkczoed.mongodb.net/')
db = client['ctf']
articles_collection = db['ctf']

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = articles_collection.find({'$text': {'$search': query}})
    articles = [{'title': article.get('title', ''), 'content': article.get('content', '')} for article in results]
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)