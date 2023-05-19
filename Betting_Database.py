from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host='127.0.0.1',
    user='student',
    password = 'student',
    database='lds_betting')
    
@app.route('/betting-lines', methods=['POST'])
def create_betting_line():
    # Retrieve data from the request
    data = request.get_json()

    # Save the data to the database
    cursor = db.cursor()
    query = "INSERT INTO betting_lines (line_name, odds) VALUES (%s, %s)"
    values = (data['line_name'], data['odds'])
    cursor.execute(query, values)
    db.commit()

    return jsonify(message='Betting line created successfully')

@app.route('/betting-lines', methods=['GET'])
def get_betting_lines():
    # Retrieve betting lines from the database
    cursor = db.cursor()
    query = "SELECT * FROM betting_lines"
    cursor.execute(query)
    result = cursor.fetchall()

    # Convert the result to a JSON response
    betting_lines = []
    for line in result:
        betting_lines.append({
            'id': line[0],
            'line_name': line[1],
            'odds': line[2]
        })

    return jsonify(betting_lines)

# Add more routes and handlers as per your app's requirements

if __name__ == '__main__':
     app.run(debug=True)
