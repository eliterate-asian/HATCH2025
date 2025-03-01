from flask import Flask, request, jsonify
import psycopg2
import numpy as np

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="motherflocker",
        user="doxa",
        password="doxa",
        host="localhost"
    )
    return conn

# Vectorize data
def vectorize_data(data):
    return np.array(list(data.values()), dtype=float)

# Dynamic column creation and data insertion
def dynamic_insert(table, data):
    conn = get_db_connection()
    cur = conn.cursor()
    columns = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table} ({columns}) VALUES ({values}) RETURNING id;"
    cur.execute(query, list(data.values()))
    row_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return row_id

# API Endpoints

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id;", (username, password))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"user_id": user_id}), 201

# Add flock data
@app.route('/flocks', methods=['POST'])
def add_flock():
    data = request.json
    required_fields = ['genus', 'species', 'gender', 'flock_size', 'flock_density']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    flock_id = dynamic_insert('flocks', data)
    return jsonify({"flock_id": flock_id}), 201

# Add infection data
@app.route('/infections', methods=['POST'])
def add_infection():
    data = request.json
    if 'flock_id' not in data:
        return jsonify({"error": "flock_id is required"}), 400

    infection_id = dynamic_insert('infections', data)
    return jsonify({"infection_id": infection_id}), 201

# Add dynamic user data
@app.route('/user_data', methods=['POST'])
def add_user_data():
    data = request.json
    if 'user_id' not in data or 'column_name' not in data or 'column_value' not in data:
        return jsonify({"error": "user_id, column_name, and column_value are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_data (user_id, column_name, column_value) VALUES (%s, %s, %s);",
                (data['user_id'], data['column_name'], data['column_value']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Data added successfully"}), 201

# Query flocks and vectorize data
@app.route('/flocks/vector', methods=['GET'])
def get_flocks_vector():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM flocks;")
    flocks = cur.fetchall()
    cur.close()
    conn.close()

    # Convert to vector
    vectorized_data = [vectorize_data(dict(row)) for row in flocks]
    return jsonify({"vectorized_data": vectorized_data})

if __name__ == '__main__':
    app.run(debug=True)
