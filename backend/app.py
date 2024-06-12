
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://localhost:27017/")
db = client['grocery_db']
deals_collection = db['deals']

class Deal(Resource):
    def get(self):
        deals = list(deals_collection.find({}, {'_id': 0}))
        return jsonify(deals)

class AddDeal(Resource):
    def post(self):
        data = request.get_json()
        deals_collection.insert_one(data)
        return {'message': 'Deal added'}, 201

class GPTChat(Resource):
    def post(self):
        user_message = request.get_json().get('message')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        return jsonify(response.choices[0].text.strip())

api.add_resource(Deal, '/deals')
api.add_resource(AddDeal, '/add-deal')
api.add_resource(GPTChat, '/chat')

if __name__ == '__main__':
    app.run(debug=True)
            