from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

app = Flask(__name__)

# Get database connection information from environment variables
db_config = {
    'host': os.getenv('MYSQL_SERVER'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DB')
}

@app.route('/')
def hello_world():
    try:
        # Attempt to connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Log successful connection
        print("Successfully connected to MySQL")

        # Retrieve all messages from the database
        cursor.execute('SELECT content FROM messages')
        messages = cursor.fetchall()

        # Close the database connection
        cursor.close()
        conn.close()

        # Return the messages as a JSON response
        return jsonify(messages=[message[0] for message in messages])

    except mysql.connector.Error as err:
        # Log any connection errors
        print(f"Error: {err}")
        return jsonify(error=str(err)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

