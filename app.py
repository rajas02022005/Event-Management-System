from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.event_management

@app.route('/')
def index():
    events = list(db.events.find())
    return render_template('index.html', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    event_data = request.json
    db.events.insert_one(event_data)
    return jsonify({'message': 'Event added successfully'}), 201

@app.route('/edit_event/<event_id>', methods=['PUT'])
def edit_event(event_id):
    updated_event = request.json
    result = db.events.update_one({'_id': ObjectId(event_id)}, {'$set': updated_event})

    if result.modified_count > 0:
        return jsonify({'message': 'Event updated successfully'}), 200
    else:
        return jsonify({'message': 'Event not found or no changes made'}), 404

@app.route('/edit_event/<event_id>', methods=['GET'])
def get_edit_event(event_id):
    event = db.events.find_one({'_id': ObjectId(event_id)})
    if event:
        return render_template('edit_event.html', event=event)
    else:
        return jsonify({'message': 'Event not found'}), 404

@app.route('/delete_event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    result = db.events.delete_one({'_id': ObjectId(event_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Event deleted successfully'}), 200
    else:
        return jsonify({'message': 'Event not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
