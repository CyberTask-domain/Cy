from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
sample_data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'},
]

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        query = request.args.get('query')
        results = [item for item in sample_data if query.lower() in item['name'].lower()]
        return jsonify(results)
    elif request.method == 'POST':
        new_item = request.json
        sample_data.append(new_item)
        return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)