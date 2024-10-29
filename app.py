from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Створюємо простий словник для збереження даних
items = []

# Ресурс для роботи з одним елементом
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item, 200
        return {'message': 'Item not found'}, 404

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}, 200

# Ресурс для роботи зі списком елементів
class ItemList(Resource):
    def post(self):
        data = request.get_json()
        new_item = {
            'name': data['name'],
            'price': data['price']
        }
        items.append(new_item)
        return new_item, 201

# Додаємо ресурси до API
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
